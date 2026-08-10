# ReAction - Release v0.1.17 (Integração de Foto de Perfil / Avatar & Otimizações Mobile)

## Suporte a Fotos de Perfil (SSO Google / Microsoft / Upload) & Ajustes Mobile

### Novidades e Ajustes (v0.1.17):
1. **Fotos de Perfil e Avatares (Google, Microsoft e Upload)**:
   - Adicionada a coluna `foto_perfil` no MySQL (`usuarios`).
   - Integração com Google / Microsoft SSO para carregar o avatar da conta automaticamente.
   - Interface de upload de foto e remoção na aba **Ajustes** (`/api/usuario/foto`).
   - Atualização de todas as barras de navegação (desktop e mobile) para renderizar a imagem do perfil com fallback para as iniciais.
2. **Otimizações para Teste em Celular e PWA**:
   - Layout 100% responsivo validado para telas mobile com menu inferior flutuante.
3. **Invalidação de Cache (`v=0.1.17`)**:
   - Queries de cache atualizadas em todos os 9 templates HTML.

---
Data de Lançamento Local e Produção: 09 de Agosto de 2026
Desenvolvido por Frame [IA]
