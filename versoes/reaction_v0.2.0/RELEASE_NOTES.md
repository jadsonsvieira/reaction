# ReAction - Release v0.2.0 (Resolução do Redirecionamento OAuth do Facebook & Documentação Meta App)

## Resolução da Mensagem "URL Bloqueada" do Facebook OAuth

### Novidades e Ajustes (v0.2.0):
1. **Redirecionamento do Facebook OAuth**:
   - Atualizada a função `iniciarFacebookLogin()` para integrar o SDK nativo do Facebook (`FB.login`) e fallback para o fluxo de redirecionamento de janela inteira (`window.location.href`), evitando bloqueios de URLs de redirecionamento em janelas pop-up.
2. **Invalidação de Cache (`v=0.2.0`)**:
   - Queries de cache atualizadas em todos os 9 templates HTML.
3. **Homologação Automatizada**:
   - Testes unitários executados com **100% de sucesso**.

---
Data de Lançamento Local e Produção: 09 de Agosto de 2026
Desenvolvido por Frame [IA]
