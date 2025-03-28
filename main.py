from logic.microphone import input_microphone
from logic.avatar import avatar_instance

import threading

def main():
    # Lanza el reconocimiento por voz en segundo plano
    hilo_microfono = threading.Thread(target=input_microphone)
    hilo_microfono.daemon = True
    hilo_microfono.start()

    # Ejecuta el mainloop en el hilo principal (requisito de Tkinter en Windows)
    avatar_instance.root.mainloop()

if __name__ == "__main__":
    main()
