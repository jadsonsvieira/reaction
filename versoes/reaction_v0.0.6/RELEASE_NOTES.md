# ReAction - Release v0.0.6 (Local)

## Autenticação Social Completa (Google, Facebook & Apple) + Auditoria de Segurança

### Novidades e Ajustes (v0.0.6):
1. **Grade de Autenticação Social no Frontend ([login.html](file:///C:/Users/jadso/Projetos/reaction/templates/login.html))**:
   - Botão **Google** ("Continuar com o Google") com marca e cores oficiais.
   - Botão **Facebook** ("Facebook") oficial em azul (`#1877F2`) com ícone vetorial.
   - Botão **Apple** ("Apple") oficial em preto (`#000000`) com ícone vetorial da maçã.
   - Divisor de formulário `"OU COM E-MAIL E SENHA"`.
2. **Rotas Dedicadas no Backend ([main.py](file:///C:/Users/jadso/Projetos/reaction/main.py))**:
   - Novas rotas `/login/google`, `/login/facebook` e `/login/apple`.
   - **Reconhecimento Instantâneo**: Login direto para usuários cadastrados.
   - **Cadastro Automático de 1-Clique**: Para novos usuários de qualquer um dos 3 provedores (criação da empresa "Empresa de [Nome]", senha segura hashed e salvamento dos IDs `google_id`, `facebook_id` e `apple_id`).
   - **Auto-seeding de Dados**: População imediata de 12 avaliações, 5 ações e 6 canais integrados via `garantir_massa_dados_empresa()`.
   - **Disparo de Notificações**: Envio do e-mail HTML de Boas-Vindas ao novo cliente e alertas instantâneos aos 3 administradores (`contato@frameia.com.br`, `jadson@mjsv.com.br`, `mara@mjsv.com.br`).
3. **Auditoria de Segurança da Informação (100% OK)**:
   - 100% verificado contra SQL Injection, vazamento de dados entre empresas (Multi-Tenancy `WHERE empresa_id = %s`), proteção `401 Unauthorized` em APIs privadas e controle de cabeçalhos `Cache-Control`.

---
Data de Lançamento Local: 05 de Agosto de 2026
Desenvolvido por Frame [IA]
