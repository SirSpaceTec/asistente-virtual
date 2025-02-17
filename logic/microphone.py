import speech_recognition as sr
from logic.model_ai import generate_short_response
from config.py_to_c import interactionOrOrder

apagar = ["apagar", "apagar asistente", "apágate"]


def input_microphone():
  count = 0
  r = sr.Recognizer()
  try:
    with sr.Microphone() as source:
      r.adjust_for_ambient_noise(source, duration=2)
      r.pause_threshold = 0.8
      r.energy_threshold = 300
      r.dynamic_energy_threshold = False
      while True:
        print(f"Di algo...")
        try:
          audio = r.listen(source, timeout=8)
          text = r.recognize_google(audio, language="es-ES")
          print(text)
          count = 0
          
          if text.lower() in apagar:
            break

          intOrOrd = interactionOrOrder(text)

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
        
        
        