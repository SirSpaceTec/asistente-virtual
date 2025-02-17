import subprocess
import os

# Diccionario de comandos y sus aplicaciones correspondientes
commands = {
  "abrir chrome": "chrome",
  "abrir firefox": "firefox",
  "abrir notepad": "notepad",
  "abrir visual estudio": "code",
  "abrir calculadora": "calc" if os.name == "nt" else "gnome-calculator"
}

def execute_command(command):
  if command in commands:
    try:
      subprocess.Popen(commands[command], shell=True)
      print(f"Executing: {command}")
    except Exception as e:
      print(f"Error al ejecutar {command}: {e}")
  else:
        return "no es un comando, pasar a chatgpt"