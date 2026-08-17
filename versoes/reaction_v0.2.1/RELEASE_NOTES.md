# Release Notes - ReAction v0.2.1
**Data:** 17/08/2026 20:27
**Versão:** v0.2.1

## Novidades e Melhorias

1. **Correção Visual do Drawer Mobile no Desktop**:
   - Adicionadas as classes `md:hidden` e `hidden` no `#mobile-menu-drawer`, eliminando o bug de renderização no rodapé de telas desktop.

2. **Integração Visual Completa do WhatsApp Bot (Padrão Cash SaaS)**:
   - Novo card em Ajustes / Perfil (`ajustes.html`): Status de conexão em tempo real (`usuario.telefone`), subpainéis de comandos (`resumo`, `acoes`, `alertas de crise`) e botão de acionamento direto no WhatsApp.
   - Nova seção na Landing Page (`index.html`): Destaque para o monitoramento 24/7 de reputação e alertas de crise em 1 minuto via WhatsApp.

3. **Higienização Integral de Segredos (GitGuardian Compliant)**:
   - Removidas todas as senhas hardcoded e chaves de API históricas de todos os arquivos e snapshots.
   - Variáveis sensíveis 100% carregadas exclusivamente via `.env`.

4. **Mesmas Credenciais do Meta Cloud API do Cash**:
   - Meta Access Token, Phone ID e Verify Token padronizados entre os ecossistemas SaaS.
