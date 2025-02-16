import speech_recognition as sr
from logic.modelAi import simular_respuesta_model

def input_microphone():
  count = 0
  r = sr.Recognizer()
  try:
    with sr.Microphone() as source:
      r.pause_threshold = 2
      r.adjust_for_ambient_noise(source, duration=1)
      while True:
        print(f"Say something, count {count}")
        try:
          audio = r.listen(source, timeout=4)
          text = r.recognize_google(audio, language="es-ES")
          print(text)
          count = 0
          if text.lower() == "apagar asistente":
            print("Apagando asistente")
            break
          # Comprobar si la interacción del usuario es una orden o una pregunta
          
          simular_respuesta_model(text)
          print("Respuesta terminada")
        except sr.WaitTimeoutError:
          print("I haven't heard anything")
        except sr.UnknownValueError:
          print("I couldn't understand the audio")
          count += 1
          if count == 3:
            break
  except OSError as e:
      print(f"Error de micrófono: {e}")
      print("Intenta reconectar tu micrófono o verifica la configuración del sistema.")
  except Exception as e:
      print(f"Ocurrió un error inesperado: {e}")
        
        
        