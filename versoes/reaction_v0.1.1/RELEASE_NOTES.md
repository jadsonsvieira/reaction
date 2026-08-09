# ReAction - Release v0.1.1 (Patch Upgrade Local)

## Exportação para Excel (.xlsx / UTF-8 BOM CSV) & Relatórios Baixáveis

### Novidades e Recursos (v0.1.1):
1. **Exportação de Avaliações em Excel ([reputacao.html](file:///C:/Users/jadso/Projetos/reaction/templates/reputacao.html))**:
   - Botão verde estilo Excel na Central de Reputação enviando o download via `/api/exportar/avaliacoes`.
   - Inclui: Data/Hora, Cliente, Canal, Nota (Estrelas), Comentário do Cliente, Sentimento, Status da Resposta e Rascunho/Resposta da IA.
2. **Exportação do Plano de Ações ([minhas_acoes.html](file:///C:/Users/jadso/Projetos/reaction/templates/minhas_acoes.html))**:
   - Botão de exportação na tela de tarefas via `/api/exportar/acoes`.
   - Inclui: Título da Ação, Prioridade (Normal/Crítica), Prazo Final, Status (Concluída/Pendente) e Data de Criação.
3. **Exportação no Painel Executivo ([relatorios.html](file:///C:/Users/jadso/Projetos/reaction/templates/relatorios.html))**:
   - Botão de download do relatório de performance diretamente em planilha.
4. **Codificação Nativa UTF-8 BOM (`ï»¿`)**:
   - Codificação nativa com separador `;` garantindo que o Microsoft Excel abra os arquivos diretamente em colunas perfeitas e com acentuação correta (`ç`, `ã`, `é`, `õ`).

---
Data de Lançamento Local: 05 de Agosto de 2026
Desenvolvido por Frame [IA]
