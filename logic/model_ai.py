from openai import OpenAI
from openai import AuthenticationError
from dotenv import load_dotenv
import os

from logic.speaker import speak_text
from logic.avatar import avatar_instance
  
  
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY") 

def check_openai_api_key(api_key = ""):
  try:
    client = OpenAI(api_key=api_key)
    client.models.list()
  except AuthenticationError:
    print("No tienes un token de acceso valido para OpenAI")
    return False
  else:
    return client
  
def generate_short_response(question):
    client = check_openai_api_key(API_KEY)
    if client:
        messages = [
            {"role": "system", "content": "Responde con frases cortas, máximo tres oraciones. Sé directo y conciso."},
            {"role": "user", "content": question}
        ]

        stream = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            stream=True,
            max_tokens=100,
            temperature=0.3,
            top_p=0.9,
            stop=["\n"]
        )

        response_text = ""
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content, end="", flush=True)
                response_text += chunk.choices[0].delta.content

        duracion_estimada = max(3, len(response_text.split()) // 2)  # Aproximación: 2 palabras por segundo
        avatar_instance.hablar(duracion=duracion_estimada)

        speak_text(response_text)
