import webbrowser
import time
import pyautogui


# Pensar como hacer la parte de la música y su control
def play_spotify_playlist(playlist_id = "37i9dQZF1DXcBWIGoYBM5M"):
    """
    Abre una playlist de Spotify usando su ID.
    """
    url = f"https://open.spotify.com/playlist/{playlist_id}"
    webbrowser.open(url) 

    time.sleep(3)
    pyautogui.press("space")