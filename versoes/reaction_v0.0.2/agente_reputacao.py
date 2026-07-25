import os
import json
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from dotenv import load_dotenv

# O pacote python-dotenv é obrigatório para extrair as chaves do arquivo oculto .env
load_dotenv()
CHAVE_API = os.environ.get("GEMINI_API_KEY")

if not CHAVE_API:
    print("Aviso: GEMINI_API_KEY não encontrada no .env")

# Definição do schema de saída estruturada para garantir a consistência dos dados do SaaS
class AnaliseAvaliacao(BaseModel):
    sentimento: str = Field(description="Sentimento da avaliação: 'positivo', 'neutro' ou 'negativo'")
    sugestao_resposta: str = Field(description="Rascunho de resposta humanizado, empático e adequado. Sem aspas adicionais.")
    tags: list[str] = Field(description="Lista de até 3 tags curtas sobre o motivo da avaliação (ex: 'atendimento lento', 'comida fria', 'elogio', 'preço alto')")

def analisar_avaliacao_gemini(nome_cliente, nota, comentario, regras_tom_voz, telefone_empresa):
    """
    Função core que envia o feedback para o Gemini e retorna o sentimento, a resposta gerada e as tags.
    Utiliza saída estruturada para evitar erros de parseamento de JSON e garantir a geração de tags.
    """
    if not comentario or comentario.strip() == "":
        comentario = "(O cliente apenas atribuiu a nota, sem deixar comentário escrito.)"

    prompt_mestre = f"""
    Você é a inteligência por trás do 'Reaction', um gestor de reputação que atua como guardião da marca e impulsionador orgânico de vendas.
    Sua tarefa é analisar a avaliação de um cliente, classificar o sentimento, gerar as tags de tópicos abordados e criar um rascunho de resposta adequado.

    DADOS DA AVALIAÇÃO:
    - Nome do Cliente: {nome_cliente}
    - Nota (1 a 5 estrelas): {nota}
    - Comentário: "{comentario}"

    SALA DE MÁQUINAS (TOM DE VOZ E REGRAS DO NEGÓCIO):
    {regras_tom_voz}

    DIRETRIZES DE EXECUÇÃO:
    1. Elogios (4 ou 5 estrelas): Gere um agradecimento humanizado e simpático.
    2. Críticas/Dúvidas (1, 2 ou 3 estrelas): Atue na contenção de crise autônoma. Nunca seja defensivo. Você DEVE obrigatoriamente incluir um CTA levando a conversa para o ambiente privado através deste link de WhatsApp: wa.me/{telefone_empresa}
    """

    try:
        # Nova estrutura da SDK do Google (genai.Client)
        client = genai.Client(api_key=CHAVE_API)
        
        # Chamada com o modelo ultra-rápido gemini-2.5-flash e saída JSON estruturada
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt_mestre,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=AnaliseAvaliacao,
            ),
        )
        
        # O retorno é garantido como um JSON válido que respeita a estrutura da classe AnaliseAvaliacao
        resultado_json = json.loads(response.text)
        return resultado_json
        
    except Exception as e:
        print(f"Erro na comunicação com o Gemini ou parseamento: {e}")
        # Fallback seguro em caso de qualquer falha
        sentimento = "positivo" if int(nota) >= 4 else "negativo" if int(nota) <= 3 else "neutro"
        if sentimento == "negativo":
            sugestao = f"Olá, {nome_cliente}. Sentimos muito pela sua experiência e queremos resolver isso. Por favor, entre em contato no wa.me/{telefone_empresa}"
        else:
            sugestao = f"Obrigado pelo seu feedback, {nome_cliente}!"
            
        return {
            "sentimento": sentimento,
            "sugestao_resposta": sugestao,
            "tags": ["Instabilidade de API"]
        }