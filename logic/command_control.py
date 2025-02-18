import subprocess
import os
import webbrowser
import time
import pyautogui
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

def execute_command(command):
  if command in commands:
    try:
      subprocess.Popen(commands[command], shell=True)
      print(f"Executing: {command}")
      return "order"
    except Exception as e:
      print(f"Error al ejecutar {command}: {e}")
  elif command in pseudo_commands:
    try:
      action = pseudo_commands[command]  # Obtiene la función o lambda
      if "abre" in command:
        open_browser(action)
      elif action in globals():  # Verifica si el método existe en el contexto global
        globals()[action]()  # Llama a la función dinámicamente
      return "order"  
      # else:
      #   return "interaction"

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

    try:
        subprocess.Popen("spotify", shell=True)
        time.sleep(3)
        pyautogui.press("space")
    except Exception as e:
        print(f"Error al abrir Spotify: {e}")

def open_browser(link):
  webbrowser.open_new_tab(link)
# # 🎵 Prueba con una playlist (ejemplo: "Today's Top Hits")
# play_spotify_playlist("37i9dQZF1DXcBWIGoYBM5M")