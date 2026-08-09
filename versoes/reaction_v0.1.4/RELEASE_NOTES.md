# ReAction - Release v0.1.4 (Patch Upgrade Local)

## Suíte de Social Logins (Google + Facebook + Apple) 100% Ativada

### Novidades e Ajustes (v0.1.4):
1. **Ativação da Suíte Completa de Social Logins ([login.html](file:///C:/Users/jadso/Projetos/reaction/templates/login.html))**:
   - Ativados e validados os 3 métodos de autenticação em 1 clique:
     - 🟡 **Google SSO**: Continuar com o Google (SDK oficial).
     - 🟦 **Facebook SSO**: Continuar com o Facebook (`#1877F2`).
     - 🖤 **Apple SSO**: Continuar com a Apple (`#000000`).
2. **Backend SSO Robusto ([main.py](file:///C:/Users/jadso/Projetos/reaction/main.py))**:
   - Rotas `/login/google`, `/login/facebook` e `/login/apple` com auto-provisionamento de empresas (`Empresa de ...`), geração de dados demonstrativos e e-mails de boas-vindas.
3. **Validação de Testes**:
   - Teste automatizado `scratch/test_social_logins.py` aprovado com 100% de sucesso (Status 302 OK para todas as rotas SSO).

---
Data de Lançamento Local: 07 de Agosto de 2026
Desenvolvido por Frame [IA]
