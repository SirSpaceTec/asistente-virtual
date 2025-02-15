import speech_recognition as sr


def input_microphone():
  count = 0
  r = sr.Recognizer()
  
  with sr.Microphone() as source:
    while True:
      print(f"Say something, count {count}")
      r.adjust_for_ambient_noise(source, duration=1)
      audio = r.listen(source, timeout=5)
      try:
        text = r.recognize_google(audio, language="es-ES")
        print(text)
        count = 0
        if text.lower() == "apagar asistente":
          print("Apagando asistente")
          break
      except sr.WaitTimeoutError:
        print("I haven't heard anything")
      except sr.UnknownValueError:
        print("I couldn't understand the audio")
        count += 1
        if count == 3:
          break