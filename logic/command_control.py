import subprocess
import os
import webbrowser
import time
import pyautogui
import shutil
import winreg
import json

control_verbs = ["pon", "ponme", "poner", "abrir", "abre", "ábreme"]

def load_commands():
  with open("commands.json", "r", encoding="utf-8") as file:
    return json.load(file)
  
data = load_commands()
commands = data.get("commands", {})
pseudo_commands = data.get("pseudo_commands", {})

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
  words = command.lower().split()
  found_verb = None
  found_command = None
  
  for word in words:
    if word in control_verbs and found_verb is None:
      found_verb = word
    elif word in commands or word in pseudo_commands:
      found_command = word
      break
    
  if found_verb and found_command:
    if found_command in commands:      
      execute_program(commands[command])
    elif found_command in pseudo_commands:
        action = pseudo_commands[found_command]  
        if action.startswith("http"):
          open_browser(action)
        elif action in globals():  # Verifica si el método existe en el contexto global
          globals()[action]()  # Llama a la función dinámicamente
    return "order"    
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


def open_browser(link):
  webbrowser.open_new_tab(link)
  