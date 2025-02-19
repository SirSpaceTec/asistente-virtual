from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os

def change_audio_speed(audio, speed=1.5):
    # Cambiar la velocidad del audio ajustando el frame_rate
    new_audio = audio._spawn(audio.raw_data, overrides={
        "frame_rate": int(audio.frame_rate * speed)
    })
    # Asegurar que el frame_rate final sea consistente
    return new_audio.set_frame_rate(audio.frame_rate)

def speak_text(text, lang="es", speed=1.3):
    # Generar el archivo de audio con gTTS en formato MP3
    tts = gTTS(text=text, lang=lang, slow=False)
    mp3_file = "response.mp3"
    tts.save(mp3_file)

    # Convertir el archivo MP3 a un objeto de audio de Pydub
    audio = AudioSegment.from_mp3(mp3_file)

    adjusted_audio = change_audio_speed(audio, speed=speed)

    # Exportar el audio ajustado a un archivo temporal
    adjusted_audio_file = "adjusted_response.wav"
    adjusted_audio.export(adjusted_audio_file, format="wav")

    play(adjusted_audio)

    os.remove(mp3_file)
    os.remove(adjusted_audio_file)

