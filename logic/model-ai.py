from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY") 

client = OpenAI(api_key=api_key)

stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
      {"role": "system", "content": "Responde con oraciones cortas y precisas."},
      {"role": "user", "content": "Donde puedo conseguir estudiar para la prueba de acceso a la universidad?"}
      ],
    stream=True,
    max_tokens=50,
    temperature=0.3
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")