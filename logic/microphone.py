import speech_recognition as sr
from logic.model_ai import simular_respuesta_model, generate_short_response
from config.py_to_c import interactionOrOrder

apagar = ["apagar", "apagar asistente", "apágate"]


def input_microphone():
  count = 0
  r = sr.Recognizer()
  try:
    with sr.Microphone() as source:
      r.pause_threshold = 2
      r.adjust_for_ambient_noise(source, duration=1)
      while True:
        print(f"Say something")
        try:
          audio = r.listen(source, timeout=4)
          text = r.recognize_google(audio, language="es-ES")
          print(text)
          count = 0
          
          if text.lower() in apagar:
            break

          intOrOrd = interactionOrOrder(text)

          if intOrOrd == "interaction":
            generate_short_response(text)

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
        
        
        