# ReAction - Release v0.1.1

## Resumo do Lançamento v0.1.1
Versão com correção de rolagem na Reputação, Tema Escuro (Dark Mode Premium), melhorias no envio de senha e massa de dados inserida no banco Hostinger de Produção.

### Novas Funcionalidades e Correções (v0.1.1):
1. **Desbloqueio de Scroll na Reputação ([reputacao.html](file:///C:/Users/jadso/Projetos/reaction/templates/reputacao.html))**: Adicionadas as classes `flex-1 h-screen overflow-y-auto relative` permitindo a rolagem vertical perfeita da página e dentro de cada coluna do Kanban.
2. **Tema Escuro (Dark Mode Obsidian)**: Implementado alternador de tema (Sol ☀️ / Lua 🌙) no menu lateral com paleta obsidian `#09090b` e salvamento de preferência no `localStorage`.
3. **Redefinição de Senha Inteligente**: Adicionado banner com opção de redefinição direta de senha na tela de login além do disparo por e-mail HTML.
4. **Massa de Dados em Produção (Hostinger MySQL)**:
   - Conectado e populado o banco remoto de produção `srv1722.hstgr.io` (`u716503964_reacao`) para todas as empresas (12 avaliações, 5 ações e 6 canais integrados por empresa).
   - Gerado o arquivo `massa_dados_producao.sql` no repositório.
5. **Repositório de Versões**: Backup completo salvo na pasta `versoes/reaction_v0.1.1/`.

---
Data de Lançamento: 25 de Julho de 2026
Desenvolvido por Frame [IA]
