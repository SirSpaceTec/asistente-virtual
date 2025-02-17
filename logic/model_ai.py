from openai import OpenAI
from dotenv import load_dotenv
import os
import tiktoken
import time

from logic.speaker import speak_text

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY") 

client = OpenAI(api_key=api_key)

total_tokens_global = 0

def count_tokens(messages, model="gpt-4o-mini"):
  encoder = tiktoken.encoding_for_model(model)
  return sum(len(encoder.encode(message["content"])) for message in messages)

def generate_short_response(question):
  global total_tokens_global
  messages=[
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
  tokens_sent = count_tokens(messages)
  # print(f"Tokens enviados: {tokens_sent}")
  
  response_text = ""
  for chunk in stream:
    if chunk.choices[0].delta.content is not None:
      print(chunk.choices[0].delta.content, end="", flush=True)
      response_text += chunk.choices[0].delta.content
      
  speak_text(response_text)
      
  tokens_received = len(tiktoken.encoding_for_model("gpt-4o-mini").encode(response_text))
  total_tokens_used = tokens_sent + tokens_received
    
  total_tokens_global += total_tokens_used
  # print(f"\nTokens utilizados en esta consulta: {total_tokens_used}")
  # print(f"Tokens totales acumulados: {total_tokens_global}") 
  
  
  
def simular_respuesta_model(question = ""):
  
  print("Procesando respuesta...")
  for i in range(3,0,-1):
    print(f"{i}...", end="", flush=True)
    time.sleep(1)
  print("\n")
  respuesta_simulada = "Esta es la respuesta del GPT simulado"
  return respuesta_simulada
