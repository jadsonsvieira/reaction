# ReAction - Release v0.1.29 (Segurança Reforçada & Correção de Vulnerabilidades)

## Vulnerabilidades Corrigidas (v0.1.29):

1. **[CRÍTICO] Correção de Vazamento do Token de Redefinição de Senha na Interface Web**:
   - Rota `/esqueci_senha` corrigida para NUNCA exibir o token ou link na tela.
   - O token é enviado **exclusivamente por e-mail** e uma mensagem genérica de segurança é exibida para prevenir enumeração de contas.
2. **[CRÍTICO] Bloqueio Estrito Contra Bypass de Autenticação OAuth (Google, Facebook, Microsoft, Apple)**:
   - Validação criptográfica obrigatória de tokens em todos os endpoints de login social (`/login/google`, `/login/facebook`, `/login/microsoft`, `/login/apple` e rotas `/api/auth/*`).
   - Bloqueado o uso de payloads avulsos sem token verificado oficialmente pelos provedores.
3. **[ALTO] Proteção e Autorização do Endpoint `/api/seed`**:
   - Endpoint restrito exigindo autenticação ativa na sessão com tenant ou chave secreta mestra administrativa (`X-Admin-Secret`).
   - Chamadas não autorizadas bloqueadas com HTTP 403 Forbidden.

---
Data de Lançamento Local e Produção: 14 de Agosto de 2026
Desenvolvido por Frame [IA]
