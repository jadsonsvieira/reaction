# ReAction - Release v0.1.12 (Correção de Conexão DB na VPS & Redefinição de Senha)

## Correção Crítica de Conexão com o Banco de Dados MySQL na VPS e Ajuste de Linguagem

### Novidades e Ajustes (v0.1.12):
1. **Injeção de Credenciais de Banco de Dados na VPS**:
   - Corrigido o ficheiro `.env` na VPS Hostinger para incluir explicitamente `DB_HOST`, `DB_USER`, `DB_PASS` e `DB_NAME`, eliminando a exceção de conexão que exibia a mensagem *"Erro temporário no servidor."*.
2. **Ajuste do Texto de Redefinição de Senha**:
   - Alterado de *"Esqueceu a palavra-passe?"* para **"Esqueceu a sua senha?"** em [templates/login.html](file:///C:/Users/jadso/Projetos/reaction/templates/login.html).
   - Padronizados todos os rótulos e mensagens do fluxo de recuperação e redefinição de senha para "Senha".
3. **Homologação Automatizada**:
   - Testes unitários executados com **100% de sucesso**.

---
Data de Lançamento Local e Produção: 09 de Agosto de 2026
Desenvolvido por Frame [IA]
