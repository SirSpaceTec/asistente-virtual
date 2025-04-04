import subprocess
import webbrowser
import shutil
import json
import sys

# Importar winreg solo si se está en Windows
if sys.platform.startswith("win"):
    import winreg
else:
    winreg = None  # Para tener una referencia en otros sistemas


# importaciones para utilizar en el globals()
from logic.services.init_services import *

control_verbs = ["pon", "ponme", "poner", "abrir", "abre", "ábreme"]

def load_commands():
  with open("commands.json", "r", encoding="utf-8") as file:
    return json.load(file)
  
data = load_commands()
commands = data.get("commands", {})
pseudo_commands = data.get("pseudo_commands", {})

# Windows
def find_program_path(app_name):
  if winreg is None:
    return None
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

def execute_command(text):
  words = text.lower().split()
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
      execute_program(commands[text])
    elif found_command in pseudo_commands:
        action = pseudo_commands[found_command]  
        if action.startswith("http"):
          open_browser(action)
        elif action in globals():  # Verifica si el método existe en el contexto global
          globals()[action]()  # Llama a la función dinámicamente
    return "order"    
  else:
    return "interaction"


def open_browser(link):
  webbrowser.open_new_tab(link)
  