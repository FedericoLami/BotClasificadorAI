import anthropic
import json

from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()

def clasicadorMensaje(mensaje):
    mensajes=[{"role": "user", "content": mensaje}]
        
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

    try:
        datos = json.loads(formato_json)
        return datos
    except json.JSONDecodeError as e:
        print("Error: Formato JSON invalido") 
        raise ValueError("La respuesta de Claude no es JSON válido")

