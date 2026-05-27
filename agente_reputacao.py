import os
import json
from google import genai
from dotenv import load_dotenv

# O pacote python-dotenv é obrigatório para extrair as chaves do arquivo oculto .env
load_dotenv()
CHAVE_API = os.environ.get("GEMINI_API_KEY")

if not CHAVE_API:
    print("Aviso: GEMINI_API_KEY não encontrada no .env")

def analisar_avaliacao_gemini(nome_cliente, nota, comentario, regras_tom_voz, telefone_empresa):
    """
    Função core que envia o feedback para o Gemini e retorna o sentimento e a resposta gerada.
    """
    if not comentario or comentario.strip() == "":
        comentario = "(O cliente apenas atribuiu a nota, sem deixar comentário escrito.)"

    prompt_mestre = f"""
    Você é a inteligência por trás do 'ReAção', um gestor de reputação que atua como guardião da marca e impulsionador orgânico de vendas.
    Sua tarefa é analisar a avaliação de um cliente, classificar o sentimento e gerar um rascunho de resposta adequado.

    DADOS DA AVALIAÇÃO:
    - Nome do Cliente: {nome_cliente}
    - Nota (1 a 5 estrelas): {nota}
    - Comentário: "{comentario}"

    SALA DE MÁQUINAS (TOM DE VOZ E REGRAS DO NEGÓCIO):
    {regras_tom_voz}

    DIRETRIZES DE EXECUÇÃO:
    1. Elogios (4 ou 5 estrelas): Gere um agradecimento humanizado e simpático.
    2. Críticas/Dúvidas (1, 2 ou 3 estrelas): Atue na contenção de crise autônoma. Nunca seja defensivo. Você DEVE obrigatoriamente incluir um CTA levando a conversa para o ambiente privado através deste link de WhatsApp: wa.me/{telefone_empresa}

    FORMATO DE SAÍDA OBRIGATÓRIO:
    Retorne EXCLUSIVAMENTE um objeto JSON válido, sem formatação markdown, contendo exatamente estas duas chaves:
    {{
        "sentimento": "positivo" | "neutro" | "negativo",
        "sugestao_resposta": "O texto da sua resposta aqui"
    }}
    """

    try:
        # Nova estrutura da SDK do Google (genai.Client)
        client = genai.Client(api_key=CHAVE_API)
        response = client.models.generate_content(
            model='gemini-1.5-flash',
            contents=prompt_mestre,
        )
        
        texto_limpo = response.text.strip().replace('```json', '').replace('```', '')
        resultado_json = json.loads(texto_limpo)
        
        return resultado_json
        
    except json.JSONDecodeError:
        print("Erro: A IA não retornou um JSON válido.")
        return {
            "sentimento": "neutro",
            "sugestao_resposta": "Obrigado pela sua avaliação. Entraremos em contacto em breve."
        }
    except Exception as e:
        print(f"Erro na comunicação com o Gemini: {e}")
        return {
            "sentimento": "neutro",
            "sugestao_resposta": "Obrigado pelo seu feedback."
        }