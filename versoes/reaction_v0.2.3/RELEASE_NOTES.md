# Release Notes • ReAction v0.2.3

> **Data:** 24 de Agosto de 2026  
> **Versão Oficial Única:** `v0.2.3`  
> **Marca:** Frame [IA] • ReAction

## Novidades & Correções Oficiais
- **Menu Inferior Mobile Centralizado (Estilo Cortana / Web3 Fintech):**
  - Barra flutuante translúcida perfeitamente centralizada na base da tela com 3 atalhos principais:
    - **Cockpit** (pílula branca ativa em destaque)
    - **Reputação** (ícone minimalista)
    - **Minhas Ações** (ícone minimalista)
  - Botão circular independente de **Menu (☰)** no canto lateral que abre suavemente o Drawer de opções avançadas (Relatórios, Sala de Máquinas, Canais & APIs, Perfil, Modo Escuro e Logout).
- **Botão "Nova Ação" com Alto Contraste:**
  - Configuração oficial do Tailwind (`tailwind.config`) injetada em todos os templates com `brand: '#ff6b35'`, garantindo o botão laranja vibrante com texto e ícone de adição (`+`) visíveis em qualquer tema.
- **Navegação Direta e Blindada:**
  - Guarda condicional `{% if usuario.termos_pendentes %}` estritamente posicionada, permitindo acesso imediato à Central de Reputação sem qualquer desvio ou modal indevido.
