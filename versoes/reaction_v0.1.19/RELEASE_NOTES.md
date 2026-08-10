# ReAction - Release v0.1.19 (Sincronização Automática de Foto de Perfil via Google, Microsoft e Facebook SSO)

## Sincronização Automática de Avatar na Autenticação SSO

### Novidades e Ajustes (v0.1.19):
1. **Google SSO**: Captura automática do parâmetro `picture` do ID Token do Google e atualização transparente no banco de dados (`usuarios.foto_perfil`) e sessão do usuário.
2. **Microsoft SSO**: Sincronização automática da foto de perfil da conta Microsoft via Unavatar/Graph API no primeiro login.
3. **Facebook SSO**: Solicitação expandida de `picture.type(large)` na Graph API do Facebook com persistência automática no perfil do usuário.
4. **Homologação Automatizada**:
   - Testes unitários executados com **100% de sucesso**.

---
Data de Lançamento Local e Produção: 09 de Agosto de 2026
Desenvolvido por Frame [IA]
