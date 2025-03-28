import speech_recognition as sr
from logic.model_ai import generate_short_response
from logic.command_control import execute_command
from logic.avatar import avatar_instance 
wake_words = ["hey asistente", "asistente"]

apagar = ["apagar", "apágate"]

def listen_for_wake_word(recognizer, source):
  print("Esperando palabra clave para activación...")
  
  while True:
    try:
      audio = recognizer.listen(source, timeout=8)
      text = recognizer.recognize_google(audio, language="es-ES").lower()
      if any(wake_word in text for wake_word in wake_words):
        print("asistente activado")
        return True
    except sr.WaitTimeoutError:
      print("No escuché nada.")
    except sr.UnknownValueError:
      print("No entendí el audio.")



def input_microphone():
  count = 0
  r = sr.Recognizer()
  try:
    with sr.Microphone() as source:
      r.adjust_for_ambient_noise(source, duration=2)
      r.pause_threshold = 0.8
      r.energy_threshold = 300
      r.dynamic_energy_threshold = False
      
      # Esperar hasta que se escuche la palabra de activación
      if not listen_for_wake_word(r, source):
          return
              
      while True:
        print(f"Di algo...")
        try:
          
          audio = r.listen(source, timeout=8)
          text = r.recognize_google(audio, language="es-ES")
          avatar_instance.pensar(duracion=2)
          print(text)
          count = 0
          
          if text.lower() in apagar:
            avatar_instance.cerrar()
            break

          intOrOrd = execute_command(text.lower())

          if intOrOrd == "interaction":
            generate_short_response(text)

        except sr.WaitTimeoutError:
          print("No escuché nada.")
        except sr.UnknownValueError:
          print("No entendí el audio.")
          count += 1
          if count == 3:
            break
 
  except OSError as e:
    print(f"Error de micrófono: {e}")
    print("Intenta reconectar tu micrófono o verifica la configuración del sistema.")
  except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
        
        
        