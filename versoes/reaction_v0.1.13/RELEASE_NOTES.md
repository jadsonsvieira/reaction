# ReAction - Release v0.1.13 (Migração para o Novo Banco MySQL `u716503964_reaction`)

## Migração Completa e Segura de Tabelas, Estrutura e Registros para o Novo Banco de Dados

### Novidades e Ajustes (v0.1.13):
1. **Migração do Banco de Dados MySQL (`u716503964_reaction`)**:
   - Transferidas todas as 6 tabelas (`empresas`, `usuarios`, `avaliacoes_feed`, `acoes`, `configuracoes_ia`, `integracoes_api`) e todos os registros mantendo relacionamentos e integridade.
   - Banco de dados configurado com o usuário `u716503964_reaction`.
2. **Atualização de Ambientes Local e VPS**:
   - Ficheiros `.env` local e na VPS Hostinger atualizados para a nova base `u716503964_reaction`.
   - Script de deploy `deploy_vps.py` atualizado.
3. **Homologação Automatizada**:
   - Executada suíte de testes com 100% de aprovação (5/5 suítes verdes).

---
Data de Lançamento Local e Produção: 09 de Agosto de 2026
Desenvolvido por Frame [IA]
