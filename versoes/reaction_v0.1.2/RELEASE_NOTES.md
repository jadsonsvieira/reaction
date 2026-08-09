# ReAction - Release v0.1.2 (Patch Upgrade Local)

## Relatório Executivo Nativo em Excel (.xlsx Multi-Abas) & Limpeza de Interface

### Novidades e Ajustes (v0.1.2):
1. **Limpeza Visual da Interface (Frontend)**:
   - Removidos os botões de exportação avulsos das telas de **Central de Reputação** ([reputacao.html](file:///C:/Users/jadso/Projetos/reaction/templates/reputacao.html)) e **Minhas Ações** ([minhas_acoes.html](file:///C:/Users/jadso/Projetos/reaction/templates/minhas_acoes.html)), mantendo a interface limpa e focada na execução de tarefas.
   - Concentrada a exportação exclusivamente na tela de **Relatórios** ([relatorios.html](file:///C:/Users/jadso/Projetos/reaction/templates/relatorios.html)) com o botão executivo **"Exportar Relatório Excel (.xlsx)"**.
2. **Geração de Arquivo Excel Nativo (`.xlsx`) com `openpyxl` em [main.py](file:///C:/Users/jadso/Projetos/reaction/main.py)**:
   - Rota `/api/exportar/relatorio_excel` gerando um **Workbook nativo do Excel com 3 abas estilizadas**:
     - **Aba 1: Resumo Executivo**: KPIs consolidados (Nota Média, Total de Avaliações, Saúde da Marca %, Avaliações Positivas/Neutras/Críticas).
     - **Aba 2: Avaliações & Feedbacks**: Tabela zebrada completa com Cliente, Canal, Nota (Estrelas), Comentário, Sentimento e Resposta da IA.
     - **Aba 3: Plano de Ações**: Tabela de tarefas de contenção de crise com Título, Prioridade, Prazo Final e Status.
3. **Formatação Profissional**:
   - Cabeçalhos estilizados com fundo escuro (`#3A3A3A`) e marca ReAction (`#FF6B35`).
   - Ajuste automático de largura de colunas para garantir leitura imediata no Excel/Google Sheets.
   - **Zero caracteres `ï»¿`** ou desconfiguração de colunas.

---
Data de Lançamento Local: 05 de Agosto de 2026
Desenvolvido por Frame [IA]
