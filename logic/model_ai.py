from openai import OpenAI
from dotenv import load_dotenv
import os

from logic.speaker import speak_text
  
  
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY") 

client = OpenAI(api_key=api_key)

total_tokens_global = 0

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
  
  response_text = ""
  for chunk in stream:
    if chunk.choices[0].delta.content is not None:
      print(chunk.choices[0].delta.content, end="", flush=True)
      response_text += chunk.choices[0].delta.content
      
  speak_text(response_text)
  
