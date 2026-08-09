# ReAction - Release v0.1.9 (Paridade Total SSO & Rotas /cadastro com Cash)

## Réplica da Arquitetura Completa de Autenticação OAuth (Google, Facebook, Microsoft) e Rotas /login e /cadastro

### Novidades e Ajustes (v0.1.9):
1. **Paridade com a Autenticação do Cash**:
   - Replicados os fluxos de login rápido via popup / SDK nativo do Google, Facebook e Microsoft MSAL para o ReAction.
   - Implementadas as rotas de API `/api/auth/google`, `/api/auth/facebook` e `/api/auth/microsoft` em [main.py](file:///C:/Users/jadso/Projetos/reaction/main.py) com retornos padronizados em JSON.
2. **Rotas `/login` e `/cadastro`**:
   - Adicionada a rota `@app.route('/cadastro', methods=['GET', 'POST'])` no backend em paridade perfeita com a rota `/login`, permitindo criar contas e navegar diretamente via URLs com sufixo `/cadastro` ou `/login`.
3. **SDKs Front-End**:
   - Adicionado o SDK MSAL da Microsoft e Google Identity Services SDK em [templates/login.html](file:///C:/Users/jadso/Projetos/reaction/templates/login.html).
4. **Homologação Automatizada**:
   - Testes unitários executados com **100% de sucesso**.

---
Data de Lançamento Local e Produção: 09 de Agosto de 2026
Desenvolvido por Frame [IA]
