import os
import json
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_USER = os.environ.get("DB_USER", "root")
DB_PASSWORD = os.environ.get("DB_PASS", "")
DB_NAME = os.environ.get("DB_NAME", "reaction_db")

def popular_banco_dados(empresa_id=1):
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cursor = conn.cursor()

    try:
        # 1. Configurações da IA na Sala de Máquinas
        cursor.execute("""
            INSERT INTO configuracoes_ia (empresa_id, tom_voz, regras_ouro, telefone_whatsapp)
            VALUES (%s, 'Profissional e empático', 'Sempre agradecer elogios destacando os pratos da casa. Em avaliações nota 1 a 3, pedir desculpas e levar a conversa imediatamente para o WhatsApp de suporte.', '5585999999999')
            ON DUPLICATE KEY UPDATE
            tom_voz = VALUES(tom_voz),
            regras_ouro = VALUES(regras_ouro),
            telefone_whatsapp = VALUES(telefone_whatsapp)
        """, (empresa_id,))

        # 2. Integrações de Canais Ativos
        plataformas = ['google', 'instagram', 'ifood', 'whatsapp', 'ze_delivery', '99food']
        for plat in plataformas:
            cursor.execute("""
                INSERT INTO integracoes_api (empresa_id, plataforma, token_acesso, status)
                VALUES (%s, %s, 'demo_token_ativo', 'ativo')
                ON DUPLICATE KEY UPDATE status = 'ativo'
            """, (empresa_id, plat))

        # 3. Limpar avaliações antigas da empresa de teste para evitar duplicados idênticos em testes repetidos
        cursor.execute("DELETE FROM avaliacoes_feed WHERE empresa_id = %s", (empresa_id,))
        cursor.execute("DELETE FROM acoes WHERE empresa_id = %s", (empresa_id,))

        # 4. Avaliações Demonstrativas (Massa de Dados Rica)
        avaliacoes = [
            {
                "plataforma": "google",
                "nome_cliente": "Mariana Souza",
                "nota": 5,
                "comentario": "Atendimento espetacular e a comida chegou super quente! Com certeza virei cliente fiel.",
                "sentimento": "positivo",
                "rascunho": "Olá Mariana! Ficamos extremamente felizes com o seu carinho. Nossa equipe trabalha diariamente para entregar o melhor serviço!",
                "tags": ["atendimento excelente", "comida quente", "fidelização"],
                "status": "respondido_ia"
            },
            {
                "plataforma": "ifood",
                "nome_cliente": "Carlos Eduardo",
                "nota": 1,
                "comentario": "O pedido demorou mais de 1h30 para entregar e chegou completamente frio. Decepcionante!",
                "sentimento": "negativo",
                "rascunho": "Olá Carlos! Pedimos imensas desculpas pelo atraso e pela temperatura do pedido. Esta não é a nossa norma. Queremos resolver isso agora mesmo com você no WhatsApp: wa.me/5585999999999",
                "tags": ["atraso na entrega", "comida fria", "crise"],
                "status": "alerta_crise"
            },
            {
                "plataforma": "instagram",
                "nome_cliente": "@beatriz_lima",
                "nota": 5,
                "comentario": "Amei a experiência de ontem no restaurante! O ambiente é lindo e os pratos são maravilhosos 😍✨",
                "sentimento": "positivo",
                "rascunho": "Muito obrigado pelo carinho, Beatriz! Adoramos ter você conosco e já estamos ansiosos pela sua próxima visita!",
                "tags": ["ambiente agradável", "prato delicioso", "instagram"],
                "status": "respondido_ia"
            },
            {
                "plataforma": "ze_delivery",
                "nome_cliente": "Rodrigo Fonseca",
                "nota": 5,
                "comentario": "Cerveja trincando de gelada e a entrega levou apenas 12 minutos! Perfeito para o futebol.",
                "sentimento": "positivo",
                "rascunho": "Valeu Rodrigo! Cerveja trincando e entrega rápida é a nossa marca registrada. Bom jogo!",
                "tags": ["cerveja gelada", "entrega ultra rápida", "zé delivery"],
                "status": "respondido_ia"
            },
            {
                "plataforma": "99food",
                "nome_cliente": "Vanessa Castro",
                "nota": 2,
                "comentario": "O entregador do 99Food deixou a bebida vazar na sacola do lanche.",
                "sentimento": "negativo",
                "rascunho": "Olá Vanessa! Lamentamos imensamente pelo incidente com a embalagem. Por favor nos chame no WhatsApp wa.me/5585999999999 para enviarmos um combo novinho imediatamente.",
                "tags": ["bebida vazou", "embalagem danificada", "99food"],
                "status": "alerta_crise"
            },
            {
                "plataforma": "ifood",
                "nome_cliente": "Fernanda Ribeiro",
                "nota": 2,
                "comentario": "Veio faltando um item do meu combo. Tentei ligar mas ninguém atendeu.",
                "sentimento": "negativo",
                "rascunho": "Olá Fernanda, sentimos muito pelo item faltante e pela falha na comunicação. Por favor, nos chame no WhatsApp wa.me/5585999999999 para fazer o reembolso imediato ou envio do item.",
                "tags": ["item faltante", "falha no suporte"],
                "status": "alerta_crise"
            },
            {
                "plataforma": "google",
                "nome_cliente": "Roberto Alves",
                "nota": 4,
                "comentario": "Comida excelente, apenas a sobremesa que achei um pouco doce demais. No geral muito bom!",
                "sentimento": "positivo",
                "rascunho": "Olá Roberto! Agradecemos o feedback e a avaliação. Vamos repassar sua observação sobre a sobremesa para o nosso chef!",
                "tags": ["comida excelente", "feedback sobremesa"],
                "status": "respondido_ia"
            },
            {
                "plataforma": "whatsapp",
                "nome_cliente": "Juliana Mendes",
                "nota": 5,
                "comentario": "Gostaria de parabenizar a equipe pelo jantar de aniversário da minha mãe! Foi impecável.",
                "sentimento": "positivo",
                "rascunho": "Olá Juliana! Ficamos honrados em fazer parte desse momento tão especial da sua família. Parabéns à sua mãe!",
                "tags": ["aniversário", "atendimento impecável"],
                "status": "respondido_ia"
            },
            {
                "plataforma": "ifood",
                "nome_cliente": "Lucas Pinheiro",
                "nota": 3,
                "comentario": "A comida é boa mas a embalagem veio meio amassada.",
                "sentimento": "neutro",
                "rascunho": "Olá Lucas! Agradecemos a observação. Já estamos alinhando com a equipe de entregas para reforçar as embalagens.",
                "tags": ["embalagem amassada", "comida saborosa"],
                "status": "alerta_crise"
            },
            {
                "plataforma": "instagram",
                "nome_cliente": "@thiago_gastronomia",
                "nota": 5,
                "comentario": "Um dos melhores pontos de carne da cidade! Recomendadíssimo.",
                "sentimento": "positivo",
                "rascunho": "Valeu demais pelo apoio, Thiago! O segredo é o carinho no preparo. Até a próxima!",
                "tags": ["ponto da carne", "recomendado"],
                "status": "respondido_ia"
            },
            {
                "plataforma": "google",
                "nome_cliente": "Camila Martins",
                "nota": 5,
                "comentario": "Preço justo, porção bem servida e atendimento rápido.",
                "sentimento": "positivo",
                "rascunho": "Obrigado Camila! É sempre um prazer servir bem e com qualidade!",
                "tags": ["preço justo", "porção servida", "rápido"],
                "status": "respondido_ia"
            },
            {
                "plataforma": "whatsapp",
                "nome_cliente": "Gabriel Torres",
                "nota": 1,
                "comentario": "Cobraram um valor diferente no cartão do que estava no cardápio.",
                "sentimento": "negativo",
                "rascunho": "Gabriel, pedimos sinceras desculpas pelo erro de cobrança. Por favor nos envie o comprovante no wa.me/5585999999999 para ajustarmos imediatamente.",
                "tags": ["erro de cobrança", "crise urgente"],
                "status": "alerta_crise"
            }
        ]

        for av in avaliacoes:
            cursor.execute("""
                INSERT INTO avaliacoes_feed (empresa_id, plataforma_origem, nome_cliente, nota, comentario, sentimento, rascunho_resposta, tags, status)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (empresa_id, av['plataforma'], av['nome_cliente'], av['nota'], av['comentario'], av['sentimento'], av['rascunho'], json.dumps(av['tags']), av['status']))

        # 5. Ações Demonstrativas em Minhas Ações
        acoes = [
            {"titulo": "Contenção de Crise: Atendimento ao cliente Carlos Eduardo (Pedido iFood frio)", "prioridade": "critical", "prazo": "2026-07-26", "status": "pendente"},
            {"titulo": "Estornar item faltante da cliente Fernanda Ribeiro (iFood)", "prioridade": "critical", "prazo": "2026-07-26", "status": "pendente"},
            {"titulo": "Verificar divergência de cobrança no cartão com o cliente Gabriel Torres", "prioridade": "critical", "prazo": "2026-07-26", "status": "pendente"},
            {"titulo": "Reunião com equipe de logística sobre embalagens amassadas", "prioridade": "normal", "prazo": "2026-07-28", "status": "pendente"},
            {"titulo": "Enviar cupom de agradecimento para cliente VIP Mariana Souza", "prioridade": "normal", "prazo": "2026-07-30", "status": "concluido"}
        ]

        for ac in acoes:
            cursor.execute("""
                INSERT INTO acoes (empresa_id, titulo, prioridade, prazo, status)
                VALUES (%s, %s, %s, %s, %s)
            """, (empresa_id, ac['titulo'], ac['prioridade'], ac['prazo'], ac['status']))

        conn.commit()
        return {
            "avaliacoes_inseridas": len(avaliacoes),
            "acoes_inseridas": len(acoes),
            "integracoes_ativas": len(plataformas)
        }

    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    print("Gerando massa de dados demonstrativa no banco...")
    resultado = popular_banco_dados()
    print(f"Sucesso! {resultado['avaliacoes_inseridas']} avaliações e {resultado['acoes_inseridas']} ações inseridas.")
