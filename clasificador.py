import anthropic
import json
from database import guardarClasificacion

from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()


msj = input("Escribi tu problema: ")

mensajes=[
    {"role": "user", "content": msj}
]

answer = client.messages.create(
    model = "claude-haiku-4-5",
    max_tokens = 1024,
    system = "Sos un clasificador de mensajes. " \
            "Respondé únicamente en formato JSON, sin texto adicional ni explicaciones. " \
            "La estructura debe ser exactamente esta: " \
            '{"categoria": "consulta/queja/urgente/spam", ' \
            '"idioma": "español/inglés/otro", ' \
            '"sentimiento": "positivo/neutral/negativo", ' \
            '"resumen": "una línea resumiendo el mensaje"}',
    messages = mensajes
    )

formato_json = answer.content[0].text
formato_json = formato_json.replace("```json", "")
formato_json = formato_json.replace("```", "")

datos = json.loads(formato_json)

print(f"""categoria: {datos['categoria']}
          idioma: {datos['idioma']}
          sentimiento: {datos['sentimiento']}
          resumen: {datos['resumen']}""")

guardarClasificacion(msj, datos["categoria"], datos["idioma"],datos["sentimiento"],datos["resumen"])