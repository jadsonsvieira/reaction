# ReAction - Release v0.1.0

## Resumo do Lançamento v0.1.0
Versão aprimorada da plataforma **ReAction** contendo serviços de e-mail transacional, redefinição de senha, roteamento direto da Landing Page e notificações automáticas de administração.

### Novas Funcionalidades e Ajustes (v0.1.0):
1. **Redirecionamento Rota Raiz**: Configurados cabeçalhos `Cache-Control: no-cache` na rota `/` e `/index.html` para garantir que `reaction.frameia.com.br` sirva diretamente a Landing Page sem redirecionar para o login.
2. **Redefinição de Senha ("Esqueci a Senha")**: Interface adicionada ao formulário de login com endpoints `/esqueci_senha` e `/redefinir_senha`.
3. **Módulo de E-mails HTML Ultra-Premium (`servico_email.py`)**:
   - **E-mail de Boas-Vindas**: Enviado com resumo de conta e credenciais para o usuário cadastrado.
   - **Notificação Administrativa (3 Destinatários)**: Disparado para `contato@frameia.com.br`, `jadson@mjsv.com.br` e `mara@mjsv.com.br` a cada novo cadastro, upgrade ou downgrade.
   - **E-mail de Redefinição de Senha**: Com link e token seguro.
4. **Integração 99Food**: Canal 99Food totalmente operacional na página de integrações e no backend.
5. **Ícones PWA Vetoriais 1:1**: Renderização de alta fidelidade a partir de `static/favicon.svg` usando engine Rust `resvg`.
6. **Repositório de Versões**: Backup integral mantido em `versoes/reaction_v0.1.0/`.

---
Data de Lançamento: 25 de Julho de 2026
Desenvolvido por Frame [IA]
