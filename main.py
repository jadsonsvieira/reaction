import os
import mysql.connector
import uuid
import requests
from flask import Flask, render_template, redirect, url_for, session, request
from datetime import date, timedelta
from dotenv import load_dotenv
from agente_reputacao import analisar_avaliacao_gemini
from werkzeug.security import generate_password_hash, check_password_hash

# Chaves das APIs (O Mundo Real)
GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")
META_APP_ID = os.environ.get("META_APP_ID")
META_APP_SECRET = os.environ.get("META_APP_SECRET")
META_VERIFY_TOKEN = os.environ.get("META_VERIFY_TOKEN", "frameia_reacao_2026")

load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Database Configuration (Mocked for now or expects environment variables)
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_USER = os.environ.get("DB_USER", "root")
DB_PASSWORD = os.environ.get("DB_PASS", "")
DB_NAME = os.environ.get("DB_NAME", "reacao_db")

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return conn
    except mysql.connector.Error as err:
        # For setup/testing purposes, handle if database doesn't exist
        if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            # Reconnect without DB_NAME to create it
            conn = mysql.connector.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD
            )
            cursor = conn.cursor()
            cursor.execute(f"CREATE DATABASE {DB_NAME}")
            conn.database = DB_NAME
            cursor.close()
            return conn
        else:
            print(f"Error connecting to database: {err}")
            return None


def criar_tabelas_se_nao_existirem():
    conn = get_db_connection()
    if not conn:
        print("Failed to get DB connection to create tables.")
        return
        
    cursor = conn.cursor()
    
    # empresas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS empresas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome_empresa VARCHAR(255) NOT NULL,
            plano_assinatura VARCHAR(50) DEFAULT 'basico',
            data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # usuarios
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            empresa_id INT NOT NULL,
            nome VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            senha VARCHAR(255) NOT NULL,
            role ENUM('dono', 'admin', 'operador') DEFAULT 'operador',
            FOREIGN KEY (empresa_id) REFERENCES empresas(id) ON DELETE CASCADE
        )
    """)
    
    # integracoes_api (ATUALIZADA v0.1.0)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS integracoes_api (
            id INT AUTO_INCREMENT PRIMARY KEY,
            empresa_id INT NOT NULL,
            plataforma ENUM('google', 'instagram', 'whatsapp', 'ifood') NOT NULL,
            token_acesso TEXT,
            token_refresh TEXT,          -- Nova coluna: Para renovar o token automaticamente
            data_expiracao DATETIME,     -- Nova coluna: Para o sistema saber quando expira
            status ENUM('ativo', 'inativo', 'erro') DEFAULT 'inativo',
            FOREIGN KEY (empresa_id) REFERENCES empresas(id) ON DELETE CASCADE
        )
    """)
    
    # avaliacoes_feed
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS avaliacoes_feed (
            id INT AUTO_INCREMENT PRIMARY KEY,
            empresa_id INT NOT NULL,
            plataforma_origem ENUM('google', 'instagram', 'whatsapp', 'ifood') NOT NULL,
            nome_cliente VARCHAR(255),
            nota INT CHECK (nota >= 1 AND nota <= 5),
            comentario TEXT,
            sentimento VARCHAR(50),          -- NOVA COLUNA
            rascunho_resposta TEXT,          -- NOVA COLUNA
            status ENUM('pendente', 'respondido_ia', 'alerta_crise') DEFAULT 'pendente',
            FOREIGN KEY (empresa_id) REFERENCES empresas(id) ON DELETE CASCADE
        )
    """)
    
    # acoes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS acoes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            empresa_id INT NOT NULL,
            criado_por INT,
            titulo VARCHAR(255) NOT NULL,
            prioridade ENUM('normal', 'critical') DEFAULT 'normal',
            prazo DATE,
            status ENUM('pendente', 'concluido') DEFAULT 'pendente',
            FOREIGN KEY (empresa_id) REFERENCES empresas(id) ON DELETE CASCADE,
            FOREIGN KEY (criado_por) REFERENCES usuarios(id) ON DELETE SET NULL
        )
    """)
    
    # configuracoes_ia (A Sala de Máquinas)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS configuracoes_ia (
            id INT AUTO_INCREMENT PRIMARY KEY,
            empresa_id INT NOT NULL UNIQUE,
            tom_voz VARCHAR(255) DEFAULT 'Profissional e empático',
            regras_ouro TEXT,
            telefone_whatsapp VARCHAR(50),
            FOREIGN KEY (empresa_id) REFERENCES empresas(id) ON DELETE CASCADE
        )
    """)

    # Criar dados Mock para evitar erro de Foreign Key no ID 1
    cursor.execute("INSERT IGNORE INTO empresas (id, nome_empresa) VALUES (1, 'Empresa Teste ReAção')")
    senha_hash = generate_password_hash('123')
    cursor.execute("INSERT IGNORE INTO usuarios (id, empresa_id, nome, email, senha) VALUES (1, 1, 'Jadson', 'admin@teste.com', %s)", (senha_hash,))

    conn.commit()
    cursor.close()
    conn.close()
    print("Database tables initialized successfully.")

# Execute initialization on startup
try:
    criar_tabelas_se_nao_existirem()
except Exception as e:
    print(f"Skipping table creation (may not have DB running yet): {e}")


@app.route('/')
def index():
    if 'usuario_id' in session:
        return redirect(url_for('app_dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        # Verifica se o utilizador existe e se a palavra-passe coincide com o hash
        if user and check_password_hash(user['senha'], senha):
            session['usuario_id'] = user['id']
            session['empresa_id'] = user['empresa_id']
            session['nome'] = user['nome']
            return redirect(url_for('app_dashboard'))
        else:
            return render_template('login.html', erro="E-mail ou palavra-passe incorretos.")
    
    return render_template('login.html')

@app.route('/registo', methods=['POST'])
def registo():
    nome_empresa = request.form.get('nome_empresa')
    nome_usuario = request.form.get('nome_usuario')
    email = request.form.get('email')
    senha = request.form.get('senha')

    if not all([nome_empresa, nome_usuario, email, senha]):
        return render_template('login.html', erro_registo="Todos os campos são obrigatórios.", mostrar_registo=True)

    # Encriptar a palavra-passe antes de guardar
    senha_hash = generate_password_hash(senha)

    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Verificar se o e-mail já está em uso
    cursor.execute("SELECT id FROM usuarios WHERE email = %s", (email,))
    if cursor.fetchone():
        cursor.close()
        conn.close()
        return render_template('login.html', erro_registo="Este e-mail já está em uso.", mostrar_registo=True)

    # 1. Criar o Tenant (A Empresa)
    cursor.execute("INSERT INTO empresas (nome_empresa) VALUES (%s)", (nome_empresa,))
    empresa_id = cursor.lastrowid

    # 2. Criar o Utilizador Dono associado à Empresa
    cursor.execute("INSERT INTO usuarios (empresa_id, nome, email, senha, role) VALUES (%s, %s, %s, %s, 'dono')", 
                   (empresa_id, nome_usuario, email, senha_hash))
    
    conn.commit()
    cursor.close()
    conn.close()

    return render_template('login.html', sucesso="Conta criada com sucesso! Pode iniciar sessão.")

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

from flask import jsonify

@app.route('/app')
def app_dashboard():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
        
    usuario = {
        'nome': session.get('nome', 'Usuário'),
        'iniciais': session.get('nome', 'U')[0].upper()
    }
    
    return render_template('dashboard.html', usuario=usuario)

@app.route('/reputacao')
def reputacao():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    return render_template('reputacao.html')

@app.route('/api/acoes', methods=['GET'])
def get_acoes():
    if 'usuario_id' not in session:
        return jsonify({"error": "Unauthorized"}), 401
    
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database error"}), 500
        
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT id as __backendId, titulo as title, 
               status = 'concluido' as completed, 
               prioridade as priority, 
               prazo as due_date
        FROM acoes
        WHERE empresa_id = %s
    """, (session.get('empresa_id'),))
    
    acoes = cursor.fetchall()
    
    # Format dates
    for acao in acoes:
        if acao['due_date']:
            acao['due_date'] = acao['due_date'].isoformat()
        acao['completed'] = bool(acao['completed'])
            
    cursor.close()
    conn.close()
    
    return jsonify(acoes)

@app.route('/api/acoes', methods=['POST'])
def create_acao():
    if 'usuario_id' not in session:
        return jsonify({"error": "Unauthorized"}), 401
        
    data = request.json
    titulo = data.get('title')
    prioridade = data.get('priority', 'normal')
    prazo = data.get('due_date') or None
    
    if not titulo:
        return jsonify({"error": "Title required"}), 400
        
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database error"}), 500
        
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO acoes (empresa_id, criado_por, titulo, prioridade, prazo, status)
        VALUES (%s, %s, %s, %s, %s, 'pendente')
    """, (session.get('empresa_id'), session.get('usuario_id'), titulo, prioridade, prazo))
    
    new_id = cursor.lastrowid
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({"__backendId": new_id}), 201

@app.route('/api/acoes/<int:acao_id>', methods=['PUT'])
def toggle_acao(acao_id):
    if 'usuario_id' not in session:
        return jsonify({"error": "Unauthorized"}), 401
        
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database error"}), 500
        
    cursor = conn.cursor()
    
    # Verify ownership
    cursor.execute("SELECT status FROM acoes WHERE id = %s AND empresa_id = %s", 
                   (acao_id, session.get('empresa_id')))
    acao = cursor.fetchone()
    
    if not acao:
        cursor.close()
        conn.close()
        return jsonify({"error": "Not found"}), 404
        
    new_status = 'pendente' if acao[0] == 'concluido' else 'concluido'
    
    cursor.execute("UPDATE acoes SET status = %s WHERE id = %s", (new_status, acao_id))
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({"success": True, "status": new_status})

@app.route('/api/acoes/<int:acao_id>', methods=['DELETE'])
def delete_acao(acao_id):
    if 'usuario_id' not in session:
        return jsonify({"error": "Unauthorized"}), 401
        
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database error"}), 500
        
    cursor = conn.cursor()
    cursor.execute("DELETE FROM acoes WHERE id = %s AND empresa_id = %s", 
                   (acao_id, session.get('empresa_id')))
    conn.commit()
    
    deleted = cursor.rowcount > 0
    cursor.close()
    conn.close()
    
    if deleted:
        return jsonify({"success": True})
    else:
        return jsonify({"error": "Not found"}), 404

@app.route('/api/webhooks/ingest', methods=['GET', 'POST'])
def webhook_ingest():
    if request.method == 'GET':
        mode = request.args.get('hub.mode')
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        
        if mode == 'subscribe' and token == META_VERIFY_TOKEN:
            return challenge, 200 # Meta aprova o webhook
        return "Acesso negado", 403
    data = request.json
    if not data:
        return jsonify({"error": "Payload inválido ou vazio"}), 400

    empresa_id = data.get('empresa_id') 
    plataforma = data.get('plataforma') 
    nome_cliente = data.get('nome_cliente', 'Cliente Anônimo')
    nota = data.get('nota')
    comentario = data.get('comentario', '')

    if not empresa_id or not plataforma or nota is None:
        return jsonify({"error": "Dados obrigatórios ausentes"}), 400

    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Falha na conexão com o banco"}), 500

    try:
        cursor = conn.cursor()
        
        # 1. Inserção Inicial: A avaliação chega crua na esteira
        cursor.execute("""
            INSERT INTO avaliacoes_feed 
            (empresa_id, plataforma_origem, nome_cliente, nota, comentario, status)
            VALUES (%s, %s, %s, %s, %s, 'pendente')
        """, (empresa_id, plataforma, nome_cliente, nota, comentario))
        
        avaliacao_id = cursor.lastrowid
        
        # 2. O Cérebro em Ação (Integração Gemini)
        # Buscar a Sala de Máquinas do cliente no banco de dados
        cursor.execute("SELECT tom_voz, regras_ouro, telefone_whatsapp FROM configuracoes_ia WHERE empresa_id = %s", (empresa_id,))
        config_ia = cursor.fetchone()
        
        if config_ia:
            regras_reais = f"Tom de voz: {config_ia[0]}. Regras obrigatórias: {config_ia[1]}"
            telefone_real = config_ia[2] or "Sem número definido"
        else:
            regras_reais = "Tom de voz profissional e empático."
            telefone_real = "WhatsApp não configurado"

        # Dispara a IA com a alma do negócio real
        resultado_ia = analisar_avaliacao_gemini(
            nome_cliente=nome_cliente,
            nota=nota,
            comentario=comentario,
            regras_tom_voz=regras_reais,
            telefone_empresa=telefone_real
        )

        sentimento = resultado_ia.get("sentimento", "neutro")
        rascunho = resultado_ia.get("sugestao_resposta", "")

        # 3. Lógica de Roteamento de Crise (Maturidade Adaptativa)
        novo_status = 'pendente'
        if nota >= 4:
            novo_status = 'respondido_ia'  # Elogios
        elif nota <= 3:
            novo_status = 'alerta_crise'   # Alerta Vermelho

        # 4. Atualização Mestra: Salva a análise da IA de volta no banco
        cursor.execute("""
            UPDATE avaliacoes_feed 
            SET sentimento = %s, rascunho_resposta = %s, status = %s
            WHERE id = %s
        """, (sentimento, rascunho, novo_status, avaliacao_id))

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({
            "success": True, 
            "message": "Avaliação processada com IA",
            "avaliacao_id": avaliacao_id,
            "sentimento": sentimento,
            "status_atribuido": novo_status
        }), 201

    except Exception as e:
        if conn:
            conn.close()
        return jsonify({"error": f"Erro interno: {str(e)}"}), 500

@app.route('/api/avaliacoes', methods=['GET'])
def get_avaliacoes():
    if 'usuario_id' not in session:
        return jsonify({"error": "Unauthorized"}), 401
    
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database error"}), 500
        
    cursor = conn.cursor(dictionary=True)
    # Buscamos as avaliações da empresa logada, da mais recente para a mais antiga
    cursor.execute("""
        SELECT id, nome_cliente as cliente, plataforma_origem as plataforma, 
               nota, comentario, rascunho_resposta as rascunho, status
        FROM avaliacoes_feed
        WHERE empresa_id = %s
        ORDER BY id DESC
    """, (session.get('empresa_id'),))
    
    avaliacoes = cursor.fetchall()
    cursor.close()
    conn.close()
    
    # Formatando para o frontend
    for av in avaliacoes:
        av['tempo'] = "Recente" # Depois podemos adicionar lógica de tempo real
        av['plataforma'] = av['plataforma'].capitalize()
        # Prevenção caso a IA ainda não tenha gerado rascunho
        if not av['rascunho']:
            av['rascunho'] = "Aguardando análise da IA..."
            
    return jsonify(avaliacoes)

@app.route('/api/avaliacoes/<int:avaliacao_id>/aprovar', methods=['PUT'])
def aprovar_avaliacao(avaliacao_id):
    if 'usuario_id' not in session:
        return jsonify({"error": "Não autorizado"}), 401

    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Erro de base de dados"}), 500

    cursor = conn.cursor()
    
    # 1. Verifica se a avaliação pertence à empresa logada (Segurança)
    cursor.execute("SELECT status FROM avaliacoes_feed WHERE id = %s AND empresa_id = %s", 
                   (avaliacao_id, session.get('empresa_id')))
    av = cursor.fetchone()

    if not av:
        cursor.close()
        conn.close()
        return jsonify({"error": "Avaliação não encontrada"}), 404

    # 2. Atualiza o status para 'respondido_ia'
    # Na Fase C (Integrações), é aqui que faremos o POST real para a API do Google/Meta
    cursor.execute("UPDATE avaliacoes_feed SET status = 'respondido_ia' WHERE id = %s", (avaliacao_id,))
    
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"success": True, "message": "Avaliação aprovada e movida com sucesso."})

@app.route('/sala_maquinas')
def sala_maquinas():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    return render_template('sala_maquinas.html')

@app.route('/api/configuracoes', methods=['GET', 'POST'])
def api_configuracoes():
    if 'usuario_id' not in session:
        return jsonify({"error": "Não autorizado"}), 401

    empresa_id = session.get('empresa_id')
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Erro de base de dados"}), 500
        
    cursor = conn.cursor(dictionary=True)

    if request.method == 'GET':
        cursor.execute("SELECT tom_voz, regras_ouro, telefone_whatsapp FROM configuracoes_ia WHERE empresa_id = %s", (empresa_id,))
        config = cursor.fetchone()
        cursor.close()
        conn.close()
        
        # Se ainda não existir configuração, devolvemos vazio
        if not config:
            return jsonify({"tom_voz": "Profissional e empático", "regras_ouro": "", "telefone_whatsapp": ""})
        return jsonify(config)

    if request.method == 'POST':
        data = request.json
        tom_voz = data.get('tom_voz', 'Profissional e empático')
        regras_ouro = data.get('regras_ouro', '')
        telefone = data.get('telefone_whatsapp', '')

        # Verifica se já existe para fazer INSERT ou UPDATE (Upsert)
        cursor.execute("SELECT id FROM configuracoes_ia WHERE empresa_id = %s", (empresa_id,))
        exists = cursor.fetchone()

        if exists:
            cursor.execute("""
                UPDATE configuracoes_ia
                SET tom_voz = %s, regras_ouro = %s, telefone_whatsapp = %s
                WHERE empresa_id = %s
            """, (tom_voz, regras_ouro, telefone, empresa_id))
        else:
            cursor.execute("""
                INSERT INTO configuracoes_ia (empresa_id, tom_voz, regras_ouro, telefone_whatsapp)
                VALUES (%s, %s, %s, %s)
            """, (empresa_id, tom_voz, regras_ouro, telefone))

        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"success": True})

@app.route('/integracoes')
def integracoes():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    return render_template('integracoes.html')

@app.route('/api/auth/<plataforma>/login')
def auth_login(plataforma):
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    
    redirect_uri = url_for('auth_callback', plataforma=plataforma, _external=True)
    
    if plataforma == 'google':
        # URL Real de Consentimento do Google
        auth_url = (f"https://accounts.google.com/o/oauth2/v2/auth?"
                    f"client_id={GOOGLE_CLIENT_ID}&"
                    f"redirect_uri={redirect_uri}&"
                    f"response_type=code&"
                    f"scope=https://www.googleapis.com/auth/business.manage&"
                    f"access_type=offline&prompt=consent")
        return redirect(auth_url)
        
    elif plataforma == 'instagram':
        # URL Real de Consentimento da Meta
        auth_url = (f"https://www.facebook.com/v18.0/dialog/oauth?"
                    f"client_id={META_APP_ID}&"
                    f"redirect_uri={redirect_uri}&"
                    f"config_id=SEU_CONFIG_ID") # Exige Config ID em apps novos
        return redirect(auth_url)

    return "Plataforma inválida", 400

@app.route('/api/auth/<plataforma>/callback')
def auth_callback(plataforma):
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
        
    empresa_id = session.get('empresa_id')
    code = request.args.get('code')
    redirect_uri = url_for('auth_callback', plataforma=plataforma, _external=True)
    
    if not code:
        return "Erro: Código não recebido ou acesso negado pelo cliente.", 400

    token_acesso = ""
    token_refresh = ""

    # Troca real do código pelo Access Token
    try:
        if plataforma == 'google':
            token_url = "https://oauth2.googleapis.com/token"
            data = {
                "code": code,
                "client_id": GOOGLE_CLIENT_ID,
                "client_secret": GOOGLE_CLIENT_SECRET,
                "redirect_uri": redirect_uri,
                "grant_type": "authorization_code"
            }
            res = requests.post(token_url, data=data).json()
            token_acesso = res.get("access_token")
            token_refresh = res.get("refresh_token", "N/A") # Google só manda se prompt=consent

        elif plataforma == 'instagram':
            token_url = "https://graph.facebook.com/v18.0/oauth/access_token"
            data = {
                "client_id": META_APP_ID,
                "redirect_uri": redirect_uri,
                "client_secret": META_APP_SECRET,
                "code": code
            }
            res = requests.get(token_url, params=data).json()
            token_acesso = res.get("access_token")
            token_refresh = "N/A" # Meta gerencia expiração de forma diferente

        if not token_acesso:
            return f"Erro ao obter token real da plataforma: {res}", 400

    except Exception as e:
        return f"Erro de comunicação com a plataforma: {str(e)}", 500
    
    # 2. Guardar a chave real no nosso Banco de Dados Blindado
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM integracoes_api WHERE empresa_id = %s AND plataforma = %s", (empresa_id, plataforma))
        existe = cursor.fetchone()
        
        if existe:
            cursor.execute("""
                UPDATE integracoes_api SET token_acesso = %s, token_refresh = %s, status = 'ativo' 
                WHERE empresa_id = %s AND plataforma = %s
            """, (token_acesso, token_refresh, empresa_id, plataforma))
        else:
            cursor.execute("""
                INSERT INTO integracoes_api (empresa_id, plataforma, token_acesso, token_refresh, status) 
                VALUES (%s, %s, %s, %s, 'ativo')
            """, (empresa_id, plataforma, token_acesso, token_refresh))
            
        conn.commit()
        cursor.close()
        conn.close()

    return redirect(url_for('integracoes', sucesso="true", plat=plataforma))

@app.route('/api/integracoes/status', methods=['GET'])
def integracoes_status():
    if 'usuario_id' not in session:
        return jsonify({"error": "Não autorizado"}), 401
        
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Erro de DB"}), 500
        
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT plataforma, status FROM integracoes_api WHERE empresa_id = %s", (session.get('empresa_id'),))
    status_db = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return jsonify(status_db)

if __name__ == '__main__':
    app.run(debug=True, port=5000)