import subprocess
import os
import webbrowser
import time
import pyautogui

import shutil
import winreg

# Diccionario de comandos y sus aplicaciones correspondientes
commands = {
  "abrir chrome": "chrome",
  "abrir firefox": "firefox",
  "abrir notepad": "notepad",
  "abrir spotify": "spotify",
  "abrir visual studio": "code",
  "abrir calculadora": "calc" if os.name == "nt" else "gnome-calculator"
}

pseudo_commands = {
  "pon música": "play_spotify_playlist",
  "abre google": "https://www.google.com",
  "abre youtube": "https://www.youtube.com",
}

# Windows
def find_program_path(app_name):
  try:
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\App Paths\\" + app_name + ".exe")
    path, _ = winreg.QueryValueEx(key, "")
    return path
  except FileNotFoundError:
    return None

# Linux/macOS
def find_program(program):
  return shutil.which(program)


def execute_program(command):
  path = find_program(command) or find_program_path(command)
  if path:
    try:
      subprocess.Popen(path, shell= True)
      print(f"Ejecutando: {command}")
      return True
    except Exception as e:
      print(f"Error al ejecutar {command}: {e}")
  return False

def execute_command(command):
  if command in commands:
    if execute_program(commands[command]):
      return "order"
    else:
      print(f"No se pudo ejecutar {command}. Verifica la instalación del programa.")
  elif command in pseudo_commands:
    try:
      action = pseudo_commands[command]  # Obtiene la función o lambda
      if "abre" in command:
        open_browser(action)
      elif action in globals():  # Verifica si el método existe en el contexto global
        globals()[action]()  # Llama a la función dinámicamente
      return "order"  
    except Exception as e:
      print(f"Error al ejecutar {command}: {e}")
  else:
    return "interaction"
      
      
      
def play_spotify_playlist(playlist_id = "37i9dQZF1DXcBWIGoYBM5M"):
    """
    Abre una playlist de Spotify usando su ID.
    """
    url = f"https://open.spotify.com/playlist/{playlist_id}"
    webbrowser.open(url) 

    time.sleep(3)
    pyautogui.press("space")

    # if execute_program("spotify"):
        # subprocess.Popen("spotify")
        # time.sleep(3)
        # pyautogui.press("space")
    # else:
        # print("Spotify no encontrado o no se pudo ejecutar.")

def open_browser(link):
  webbrowser.open_new_tab(link)
  