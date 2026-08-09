# ReAction - Release v0.1.7 (Microsoft SSO & OAuth Suite)

## Substituição da Apple pelo Microsoft SSO com Credenciais Compartilhadas do Cash

### Novidades e Ajustes (v0.1.7):
1. **Substituição da Autenticação Apple por Microsoft SSO**:
   - A tela de autenticação e registo de conta ([templates/login.html](file:///C:/Users/jadso/Projetos/reaction/templates/login.html)) foi atualizada trocando o botão Apple pelo **botão oficial Microsoft** (ícone quadricolor de 4 blocos).
2. **Integração Backend da Rota `/login/microsoft`**:
   - Implementada a rota `/login/microsoft` em [main.py](file:///C:/Users/jadso/Projetos/reaction/main.py) com criação automática de conta, associação da coluna `microsoft_id` e atribuição de papel `dono`.
3. **Credenciais OAuth do Cash**:
   - Importadas as credenciais oficiais do Cash no arquivo [.env](file:///C:/Users/jadso/Projetos/reaction/.env): `MICROSOFT_CLIENT_ID="138269ce-38e6-4c1e-bc6a-b5292e877a24"`.
4. **Homologação Automatizada**:
   - Testes unitários e auditoria executados com **100% de sucesso (6/6 testes verdes)**.

---
Data de Lançamento Local e Produção: 09 de Agosto de 2026
Desenvolvido por Frame [IA]
