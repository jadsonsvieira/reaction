import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

SMTP_HOST = os.environ.get("SMTP_HOST", "smtp.hostinger.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", 587))
SMTP_USER = os.environ.get("SMTP_USER", "contato@frameia.com.br")
SMTP_PASS = os.environ.get("SMTP_PASS", "")

ADMIN_EMAILS = [
    "contato@frameia.com.br",
    "jadson@mjsv.com.br",
    "mara@mjsv.com.br"
]

def _enviar_email_html(destinatarios, assunto, html_content):
    """Função utilitária interna para disparar e-mail em HTML via SMTP"""
    if isinstance(destinatarios, str):
        destinatarios = [destinatarios]

    print(f"\n[SERVICO DE E-MAIL] Disparando e-mail para: {', '.join(destinatarios)}")
    
    if not SMTP_PASS or SMTP_PASS == "sua_senha_smtp_aqui":
        print("[SISTEMA E-MAIL] Configuração SMTP não preenchida no .env. E-mail simulado com sucesso!")
        return True

    try:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = assunto
        msg['From'] = f"ReAction IA <{SMTP_USER}>"
        msg['To'] = ", ".join(destinatarios)

        part_html = MIMEText(html_content, 'html', 'utf-8')
        msg.attach(part_html)

        server = smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=10)
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.sendmail(SMTP_USER, destinatarios, msg.as_string())
        server.quit()
        print("[SERVIÇO DE E-MAIL] E-mail enviado via SMTP com sucesso!")
        return True
    except Exception as e:
        print(f"[ERRO E-MAIL] Falha ao enviar e-mail via SMTP: {e}")
        return False

def enviar_email_boas_vindas(user_email, nome_usuario, empresa_nome):
    """Envia um e-mail de boas-vindas elegante para o usuário recém-cadastrado"""
    assunto = f"Bem-vindo ao ReAction, {nome_usuario}! Sua marca está protegida 🛡️"
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {{ font-family: 'Segoe UI', Helvetica, Arial, sans-serif; background-color: #0c0d0e; color: #e4e4e7; margin: 0; padding: 0; }}
            .container {{ max-width: 600px; margin: 30px auto; background-color: #141517; border-radius: 24px; border: 1px solid #27272a; overflow: hidden; box-shadow: 0 20px 40px rgba(0,0,0,0.5); }}
            .header {{ background: linear-gradient(135deg, #ff6b35 0%, #e05524 100%); padding: 40px 30px; text-align: center; color: #ffffff; }}
            .header h1 {{ margin: 0; font-size: 28px; font-weight: 800; tracking-tight: -0.5px; }}
            .content {{ padding: 35px 30px; line-height: 1.6; color: #d4d4d8; }}
            .card {{ background-color: #1f2023; border-radius: 16px; border: 1px solid #27272a; padding: 20px; margin: 25px 0; }}
            .card-item {{ display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px solid #2d2f34; font-size: 14px; }}
            .card-item:last-child {{ border-bottom: none; }}
            .btn {{ display: inline-block; background: linear-gradient(135deg, #ff6b35 0%, #e05524 100%); color: #ffffff !important; text-decoration: none; padding: 16px 36px; border-radius: 14px; font-weight: 700; font-size: 16px; margin: 25px 0; text-align: center; box-shadow: 0 10px 20px rgba(255,107,53,0.3); }}
            .footer {{ background-color: #0c0d0e; padding: 25px; text-align: center; font-size: 12px; color: #71717a; border-top: 1px solid #1f2023; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <div style="font-size: 40px; margin-bottom: 10px;">🛡️</div>
                <h1>ReAction</h1>
                <p style="margin: 5px 0 0 0; opacity: 0.9; font-size: 14px;">Gestão de Reputação e Contenção de Crises com IA</p>
            </div>
            <div class="content">
                <h2 style="color: #ffffff; font-size: 20px; margin-top: 0;">Olá, {nome_usuario}!</h2>
                <p>É com enorme satisfação que recebemos a <strong>{empresa_nome}</strong> no ReAction. A partir de agora, a sua Inteligência Artificial cuidará das suas avaliações 24/7, blindando a sua marca contra crises e engajando clientes satisfeitos.</p>

                <div class="card">
                    <h3 style="color: #ff6b35; margin-top: 0; font-size: 15px; text-transform: uppercase;">Resumo da sua Conta:</h3>
                    <div class="card-item"><span style="color: #a1a1aa;">Empresa:</span> <strong style="color: #ffffff;">{empresa_nome}</strong></div>
                    <div class="card-item"><span style="color: #a1a1aa;">E-mail de Acesso:</span> <strong style="color: #ffffff;">{user_email}</strong></div>
                    <div class="card-item"><span style="color: #a1a1aa;">Plano Ativo:</span> <strong style="color: #4ade80;">Shield Start (Freemium)</strong></div>
                </div>

                <div style="text-align: center;">
                    <a href="https://reaction.frameia.com.br/login" class="btn">Acessar Meu Painel ReAction →</a>
                </div>

                <p style="font-size: 13px; color: #a1a1aa; margin-top: 25px;">Dica: Acesse a <strong>Sala de Máquinas</strong> no seu painel para calibrar o tom de voz da IA e cadastrar as suas regras de ouro de atendimento.</p>
            </div>
            <div class="footer">
                &copy; 2026 ReAction — Inteligência Artificial para Reputação Online.<br>
                Desenvolvido por <strong>Frame [IA]</strong>
            </div>
        </div>
    </body>
    </html>
    """
    return _enviar_email_html(user_email, assunto, html)

def enviar_notificacao_admin(tipo_evento, dados):
    """Envia uma notificação em HTML de alta fidelidade para os 3 administradores sobre novos usuários ou mudanças de plano"""
    
    titulos = {
        "novo_usuario": "🎉 Novo Cadastro Realizado no ReAction",
        "upgrade": "🚀 Upgrade de Plano Confirmado",
        "downgrade": "⚠️ Alteração de Plano Registrada"
    }
    
    assunto = titulos.get(tipo_evento, f"🔔 Notificação Administrativa ReAction - {tipo_evento}")
    
    nome_cliente = dados.get('nome_usuario', 'Cliente')
    email_cliente = dados.get('email', '-')
    empresa = dados.get('nome_empresa', '-')
    plano = dados.get('plano', 'Freemium')
    ciclo = dados.get('ciclo', 'Mensal')
    valor = dados.get('valor', 'R$ 0,00')

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {{ font-family: 'Segoe UI', Helvetica, Arial, sans-serif; background-color: #09090b; color: #e4e4e7; margin: 0; padding: 0; }}
            .container {{ max-width: 600px; margin: 30px auto; background-color: #121316; border-radius: 20px; border: 1px solid #27272a; overflow: hidden; }}
            .header {{ background: #1f2023; border-bottom: 2px solid #ff6b35; padding: 25px 30px; text-align: left; }}
            .badge {{ display: inline-block; background-color: #ff6b35; color: #ffffff; padding: 4px 12px; border-radius: 99px; font-size: 11px; font-weight: 800; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px; }}
            .content {{ padding: 30px; }}
            .table-box {{ width: 100%; border-collapse: collapse; margin-top: 20px; font-size: 14px; }}
            .table-box td {{ padding: 12px 15px; border-bottom: 1px solid #27272a; color: #d4d4d8; }}
            .table-box td:first-child {{ color: #a1a1aa; font-weight: 600; width: 35%; }}
            .footer {{ background-color: #09090b; padding: 20px; text-align: center; font-size: 12px; color: #71717a; border-top: 1px solid #1f2023; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <div class="badge">Painel Administrativo</div>
                <h2 style="color: #ffffff; margin: 0; font-size: 20px;">{assunto}</h2>
            </div>
            <div class="content">
                <p style="margin-top: 0; color: #a1a1aa;">Atenção equipe, um novo evento de conta foi registrado na plataforma ReAction:</p>

                <table class="table-box">
                    <tr><td>Cliente / Responsável:</td><td><strong style="color: #ffffff;">{nome_cliente}</strong></td></tr>
                    <tr><td>E-mail:</td><td><a href="mailto:{email_cliente}" style="color: #ff6b35; text-decoration: none;">{email_cliente}</a></td></tr>
                    <tr><td>Nome da Empresa:</td><td><strong style="color: #ffffff;">{empresa}</strong></td></tr>
                    <tr><td>Plano Contratado:</td><td><strong style="color: #4ade80;">{plano} ({ciclo})</strong></td></tr>
                    <tr><td>Valor Estimado:</td><td><strong style="color: #ffffff;">{valor}</strong></td></tr>
                </table>

                <div style="margin-top: 30px; padding: 15px; background-color: #1f2023; border-radius: 12px; font-size: 13px; color: #a1a1aa; text-align: center;">
                    Notificação automática enviada para: <strong>contato@frameia.com.br</strong>, <strong>jadson@mjsv.com.br</strong> e <strong>mara@mjsv.com.br</strong>.
                </div>
            </div>
            <div class="footer">
                &copy; 2026 ReAction Admin Monitor • Frame [IA]
            </div>
        </div>
    </body>
    </html>
    """
    return _enviar_email_html(ADMIN_EMAILS, assunto, html)

def enviar_email_redefinicao_senha(user_email, nome_usuario, token_link):
    """Envia um e-mail elegante para solicitação de redefinição de senha"""
    assunto = "Redefinição de Senha — ReAction"
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {{ font-family: 'Segoe UI', Helvetica, Arial, sans-serif; background-color: #0c0d0e; color: #e4e4e7; margin: 0; padding: 0; }}
            .container {{ max-width: 600px; margin: 30px auto; background-color: #141517; border-radius: 24px; border: 1px solid #27272a; overflow: hidden; }}
            .header {{ background: linear-gradient(135deg, #1f2023 0%, #0c0d0e 100%); padding: 35px 30px; text-align: center; border-bottom: 2px solid #ff6b35; }}
            .content {{ padding: 35px 30px; line-height: 1.6; color: #d4d4d8; }}
            .btn {{ display: inline-block; background: linear-gradient(135deg, #ff6b35 0%, #e05524 100%); color: #ffffff !important; text-decoration: none; padding: 16px 36px; border-radius: 14px; font-weight: 700; font-size: 16px; margin: 25px 0; text-align: center; shadow: 0 10px 20px rgba(255,107,53,0.3); }}
            .footer {{ background-color: #0c0d0e; padding: 25px; text-align: center; font-size: 12px; color: #71717a; border-top: 1px solid #1f2023; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1 style="color: #ff6b35; margin: 0; font-size: 24px;">ReAction</h1>
                <p style="color: #a1a1aa; margin: 5px 0 0 0; font-size: 13px;">Redefinição de Palavra-passe / Senha</p>
            </div>
            <div class="content">
                <h2 style="color: #ffffff; font-size: 18px; margin-top: 0;">Olá, {nome_usuario}.</h2>
                <p>Recebemos um pedido para redefinir a senha da sua conta no ReAction. Se você fez essa solicitação, clique no botão abaixo para escolher uma nova palavra-passe:</p>

                <div style="text-align: center;">
                    <a href="{token_link}" class="btn">Redefinir Minha Senha Agora →</a>
                </div>

                <p style="font-size: 12px; color: #71717a; margin-top: 30px;">Se você não solicitou a redefinição de senha, ignore este e-mail com segurança. Sua senha atual permanecerá inalterada.</p>
            </div>
            <div class="footer">
                &copy; 2026 ReAction — Suporte e Segurança.<br>
                Desenvolvido por <strong>Frame [IA]</strong>
            </div>
        </div>
    </body>
    </html>
    """
    return _enviar_email_html(user_email, assunto, html)
