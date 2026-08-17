# ReAction SaaS - Release v0.2.0
**Data de Publicação:** 17/08/2026 07:42:38
**Empresa Mantenedora:** MJSV TECNOLOGIA E SOLUCOES DIGITAIS INOVA SIMPLES (I.S.)
**CNPJ:** 68.614.850/0001-13

## Novidades e Melhorias desta Versão (v0.2.0):
1. **Integração Jurídica & LGPD Oficial**:
   - Inclusão dos novos Termos de Uso (`/termos`) e Política de Privacidade & LGPD (`/privacidade`) com Razão Social e CNPJ `68.614.850/0001-13`.
   - Modal de aceite obrigatório bloqueante para consentimento expresso de usuários ativos (`/api/aceitar_termos`).
   - Checkbox de consentimento prévio no cadastro de novos clientes.
2. **Integração Completa com WhatsApp Bot (Meta Cloud API)**:
   - Endpoint de Webhook `/webhook` (GET para handshake de segurança Meta e POST para processamento de mensagens).
   - Comandos inteligentes para gestores: `resumo` / `reputacao`, `acoes` / `tarefas`, `criar acao [texto]`, `alertas` (crises de nota 1-2 estrelas) e `ajuda`.
   - Campo para cadastro do WhatsApp nos Ajustes do Perfil do usuário.
3. **Dock Flutuante Mobile 100% Simétrico & Action Sheet Drawer**:
   - Layout em grade `grid grid-cols-4` garantindo que todos os 4 botões (Cockpit, Reputação, Ações, Menu) tenham largura matematicamente igual (25% cada), eliminando qualquer deslocamento ou assimetria.
4. **Setup VIP ReAction Atualizado**:
   - Remoção de cláusulas de período isento/mensalidade grátis, mantendo foco na calibração personalizada da IA e consultoria ao vivo.
5. **Ajuste de Identidade Visual**:
   - Remoção de blocos brancos nos logos de topo e sidebar, mantendo a logo transparente oficial em todas as abas nos temas claro e escuro.
