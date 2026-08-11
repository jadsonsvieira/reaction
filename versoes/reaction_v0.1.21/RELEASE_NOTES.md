# ReAction - Release v0.1.21 (Correção Definitiva do Microsoft SSO & Decodificação JWT)

## Resolução da Identificação de E-mail na Autenticação Microsoft (v0.1.21)

### Novidades e Ajustes (v0.1.21):
1. **Extração de Claims MSAL no Client-Side**:
   - Atualizada a função `iniciarMicrosoftLogin()` em `login.html` para ler e enviar `res.account.username` e `res.idTokenClaims` (preferred_username/email/upn) na requisição AJAX `/api/auth/microsoft`.
2. **Decodificação de Token JWT no Server-Side (`main.py`)**:
   - Inserida decodificação nativa do JWT Token da Microsoft em `login_microsoft()` para capturar e-mail e nome caso o acesso seja feito via ID Token sem autorização do Graph API.
3. **Invalidação de Cache (`v=0.1.21`)**:
   - Queries de cache atualizadas em todos os 9 templates HTML.
4. **Homologação Automatizada**:
   - Testes unitários executados com **100% de sucesso**.

---
Data de Lançamento Local e Produção: 10 de Agosto de 2026
Desenvolvido por Frame [IA]
