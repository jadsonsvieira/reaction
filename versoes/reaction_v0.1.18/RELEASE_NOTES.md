# ReAction - Release v0.1.18 (Correção da Rota `/api/usuario/foto` de Upload de Foto de Perfil)

## Correção Crítica na Rota de Upload de Foto de Perfil

### Novidades e Ajustes (v0.1.18):
1. **Posicionamento de Rotas no Flask**:
   - Movidas as rotas `@app.route('/api/usuario/foto')` e `@app.route('/api/usuario/foto/remover')` para antes do bloco `if __name__ == '__main__':`.
2. **Resolução da Dependência de Geração Nítida de Nomes**:
   - Substituída a chamada `secrets.token_hex(4)` por `os.urandom(4).hex()`.
3. **Criação Automática do Diretório de Uploads (`static/uploads/avatars/`)**:
   - Garantida a criação física da pasta de imagens de avatar no servidor Hostinger VPS.
4. **Homologação Automatizada**:
   - Testes unitários executados com **100% de sucesso**.

---
Data de Lançamento Local e Produção: 09 de Agosto de 2026
Desenvolvido por Frame [IA]
