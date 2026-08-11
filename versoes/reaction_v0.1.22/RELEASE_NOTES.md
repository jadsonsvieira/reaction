# ReAction - Release v0.1.22 (Ajuste de Layout Mobile, Sanitização de Segredos e Testes 100% OK)

## Novidades e Ajustes (v0.1.22):

1. **Ajuste de Layout Mobile da Landing Page (`templates/index.html`)**:
   - Correção do vazamento/overflow lateral direito no celular através do contêiner `relative w-full overflow-hidden min-h-screen`, `max-width: 100%`, `overflow-wrap: break-word` e contenção de efeitos `glow-effect`.
2. **Segurança de Código e Sanitização de Segredos**:
   - Atualização do `.gitignore` e sanitização automática de credenciais nos scripts de snapshot para evitar alertas do GitHub Secret Scanning e GitGuardian.
3. **Validação das 3 Plataformas de Login (Google, Facebook, Microsoft)**:
   - Validados fluxos de criação de conta e login social para Google, Facebook e Microsoft com **100% de sucesso**.
4. **Invalidação de Cache (`v=0.1.22`)**:
   - Queries de cache atualizadas em todos os 9 templates HTML.

---
Data de Lançamento Local e Produção: 10 de Agosto de 2026
Desenvolvido por Frame [IA]
