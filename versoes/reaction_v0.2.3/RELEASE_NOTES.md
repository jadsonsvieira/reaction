# Release Notes • reaction_v0.2.3

> **Data:** 24 de Agosto de 2026  
> **Versão:** `v0.2.3`  
> **Marca:** Frame [IA] • ReAction

## Correções & Melhorias
- **Botão "Nova Ação" com Alto Contraste:** Restaurado o background `bg-brand` com texto branco em negrito e ícone de adição (`plus`), garantindo perfeita visibilidade e nitidez tanto no modo claro quanto no modo escuro.
- **Blindagem do Modal de Termos LGPD:** Inserida a guarda condicional `{% if usuario.termos_pendentes %}` em `reputacao.html` e `relatorios.html`, eliminando o desvio involuntário para termos ao navegar para a Central de Reputação.
- **Injeção Padronizada de Tailwind & Lucide:** Adicionado o bloco `tailwind.config` com a paleta da marca (`brand: '#ff6b35'`, `sidebar: '#3a3a3a'`, `bglight: '#f4f4f5'`) em todos os templates internos.
- **Menu Inferior Mobile Centralizado (3 Itens + Bolinha Menu):** Dock minimalista centralizado com 3 atalhos principais (`Cockpit`, `Reputação`, `Ações`) com pílula ativa e botão circular de Menu no canto com ícone `menu` SVG.
