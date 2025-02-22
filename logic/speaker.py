from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os
from dotenv import load_dotenv
import sys
import subprocess

load_dotenv()
PATH_FFMPEG = os.getenv("PATH_FFMPEG")

if PATH_FFMPEG:
    AudioSegment.converter = PATH_FFMPEG

def play_audio_mac(file_path):
    try:
        subprocess.run(["afplay", file_path], check=True)
    except subprocess.CalledProcessError as e:
        print("Error reproduciendo el audio:", e)

def change_audio_speed(audio, speed=1.5):
    new_audio = audio._spawn(audio.raw_data, overrides={
        "frame_rate": int(audio.frame_rate * speed)
    })
    return new_audio.set_frame_rate(audio.frame_rate)

def speak_text(text, lang="es", speed=1.3):
    tts = gTTS(text=text, lang=lang, slow=False)
    mp3_file = "response.mp3"
    tts.save(mp3_file)

    audio = AudioSegment.from_mp3(mp3_file)

    adjusted_audio = change_audio_speed(audio, speed=speed)

    adjusted_audio_file = "adjusted_response.wav"
    adjusted_audio.export(adjusted_audio_file, format="wav")
    if sys.platform.startswith("win"): #windows
        play(adjusted_audio)
    elif sys.platform.startswith("darwin"): #macOS
        play_audio_mac(adjusted_audio_file)

    os.remove(mp3_file)
    os.remove(adjusted_audio_file)

