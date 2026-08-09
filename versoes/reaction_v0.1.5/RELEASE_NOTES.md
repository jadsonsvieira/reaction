# ReAction - Release v0.1.5 (Security Release Local)

## Blindagem Completa de Segurança e Correção de Vulnerabilidades

### Vulnerabilidades Corrigidas (v0.1.5):
1. **Blindagem Contra Sequestro de Conta (`/redefinir_senha`) [🔴 CRÍTICO]**:
   - Implementadas as colunas `reset_token VARCHAR(255)` e `reset_expires DATETIME` no MySQL.
   - A rota `/esqueci_senha` agora gera **tokens criptográficos únicos de alta entropia** (`secrets.token_urlsafe(32)`) válidos por 30 minutos.
   - As rotas `GET/POST /redefinir_senha` agora **exigem obrigatoriamente** o token válido e não expirado. Qualquer tentativa sem token é bloqueada.
2. **Eliminação do Bypass de Autenticação SSO [🔴 CRÍTICO]**:
   - Removidos 100% dos fallbacks automáticos para contas compartilhadas (`usuario.google@frameia.com.br`, etc.).
   - As rotas `/login/google`, `/login/facebook` e `/login/apple` passam a exigir obrigatoriamente credenciais válidas e assinadas pelo provedor OAuth.
3. **Fechamento do Servidor & Desativação do Debug Mode [🟠 ALTO]**:
   - O aplicativo Flask em `main.py` foi configurado para ler `FLASK_DEBUG` (padrão `False`) e `FLASK_HOST` (padrão `127.0.0.1`), garantindo que o console Werkzeug não fique exposto em redes públicas.
4. **Proteção em Webhooks**:
   - Adicionada validação de segredo/token na recepção de payloads.
5. **Homologação Automatizada**:
   - Suíte de auditoria `scratch/test_saas_security_v015.py` executada com **100% de sucesso**.

---
Data de Lançamento Local: 07 de Agosto de 2026
Desenvolvido por Frame [IA]
