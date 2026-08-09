# ReAction - Release v0.1.3 (Patch Upgrade Local)

## Menu Mobile Hambúrguer, Correção de Proporção & Impressão PDF

### Novidades e Ajustes (v0.1.3):
1. **Menu Mobile Hambúrguer na Landing Page ([index.html](file:///C:/Users/jadso/Projetos/reaction/templates/index.html))**:
   - Adicionado botão hambúrguer no topo direito da barra de navegação no celular (estilo Cash).
   - Menu suspenso com navegação fluida (*A Solução*, *Funcionalidades*, *Como Funciona*, *Planos*, *Entrar*, *Começar Grátis*).
2. **Correção de Proporção e Enquadramento Mobile**:
   - Trava de overflow lateral (`overflow-x-hidden !important; max-width: 100vw !important;`).
   - Enquadramento 100% proporcional e centralizado sem arrastar ou puxar para a direita em qualquer modelo de smartphone.
3. **Correção da Impressão de PDF ([relatorios.html](file:///C:/Users/jadso/Projetos/reaction/templates/relatorios.html))**:
   - Reformuladas as regras `@media print` para **A4 Portrait**.
   - Removida a limitação de altura `100vh`, permitindo que o PDF imprima o relatório completo sem cortar gráficos ou tabelas.
   - Adicionada a regra `break-inside: avoid; page-break-inside: avoid;` para impedir quebras no meio de cartões KPI.
4. **Calibração de Texto no Botão de Excel**:
   - Texto ajustado para **"Exportar Relatório Excel"** (removido o sufixo `.xlsx`).

---
Data de Lançamento Local: 05 de Agosto de 2026
Desenvolvido por Frame [IA]
