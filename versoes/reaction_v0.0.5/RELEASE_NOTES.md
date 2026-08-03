# ReAction - Release v0.0.5

## Login e Cadastro com a Conta do Google (Google Single Sign-On / SSO)

### Novas Funcionalidades (v0.0.5):
1. **Autenticação de 1-Clique via Google ([login.html](file:///C:/Users/jadso/Projetos/reaction/templates/login.html))**:
   - Integração com a biblioteca oficial do Google Identity Services (GSI SDK).
   - Botão "Continuar com o Google" oficial e responsivo para Login e Cadastro.
2. **Fluxo Automático de Login e Registro no Backend ([main.py](file:///C:/Users/jadso/Projetos/reaction/main.py))**:
   - Nova rota `/login/google` para validação de ID Token do Google.
   - **Login direto** para usuários existentes.
   - **Cadastro automático de 1-Clique** para novos clientes: criação da empresa, hashing de senha segura e atribuição do `google_id`.
   - **Auto-seeding de Dados**: População instantânea de 12 avaliações, 5 ações e 6 canais via `garantir_massa_dados_empresa()`.
   - **Disparo de E-mails**: Envio do e-mail HTML de Boas-Vindas ao cliente e alerta instantâneo aos 3 administradores (`contato@frameia.com.br`, `jadson@mjsv.com.br`, `mara@mjsv.com.br`).

---
Data de Lançamento: 02 de Agosto de 2026
Desenvolvido por Frame [IA]
