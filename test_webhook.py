import requests
import json

url = "http://localhost:5000/api/webhooks/ingest"

payload = {
    "empresa_id": 1,
    "plataforma": "google",
    "nome_cliente": "Cliente Fúria",
    "nota": 1,
    "comentario": "Comida horrível e atendimento péssimo. Nunca mais volto!"
}

headers = {
    "Content-Type": "application/json"
}

print("A enviar avaliação simulada para o Webhook...")
response = requests.post(url, data=json.dumps(payload), headers=headers)

print(f"Status Code: {response.status_code}")
print("Resposta do Servidor:")
print(json.dumps(response.json(), indent=2, ensure_ascii=False))