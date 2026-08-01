# ReAction - Release v0.0.4

## Resumo das Novidades do Lançamento v0.0.4

### 1. Banner Setup VIP Dismissível & Lógica Anti-Flash ([dashboard.html](file:///C:/Users/jadso/Projetos/reaction/templates/dashboard.html))
- Adicionado botão de fechar (`X`) no banner escuro de onboarding do Setup VIP no Cockpit.
- Preferência de ocultação salva no navegador (`localStorage.setItem('hideSetupVipReAction', 'true')`).
- Lógica anti-flash síncrona no `<head>` usando a classe `.hide-setup-vip` para garantir 0 piscadas ao navegar entre as abas.
- Correção e restauração da estrutura visual do Tailwind CSS e das seções do Dashboard.

### 2. Otimização da Tela de Ajustes ([ajustes.html](file:///C:/Users/jadso/Projetos/reaction/templates/ajustes.html))
- Transformação do layout para um **Grid Responsivo de 2 Colunas** (`max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-8`), eliminando a área branca vazia em telas desktop.
- Card exclusivo de **WhatsApp do Gerente / Vendedor (Alertas de Crise 1-2 estrelas)** para envio de ponte privada via WhatsApp.
- Card Permanente do **Setup VIP ReAction (R$ 300,00 à vista)**.

---
Data de Lançamento: 01 de Agosto de 2026
Desenvolvido por Frame [IA]
