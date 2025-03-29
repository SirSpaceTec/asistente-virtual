import tkinter as tk
from PIL import Image, ImageTk
import threading
import time

class AvatarApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Asistente Virtual")
        self.root.geometry("1024x1024")
        self.root.resizable(False, False)

        self.image1 = ImageTk.PhotoImage(Image.open("avatar_boca_cerrada.png"))
        self.image2 = ImageTk.PhotoImage(Image.open("avatar_boca_abierta.png"))
        self.image_pensando = ImageTk.PhotoImage(Image.open("avatar_pensando.png"))


        self.label = tk.Label(self.root, image=self.image1)
        self.label.pack()

        self.talking = False

    def hablar(self, duracion=5):
      def animacion():
          self.talking = True
          tiempo = time.time()
          while time.time() - tiempo < duracion:
              self.label.config(image=self.image2)
              self.root.update()
              time.sleep(0.2)
              self.label.config(image=self.image1)
              self.root.update()
              time.sleep(0.2)
          self.talking = False
      
      threading.Thread(target=animacion).start()
          
    def pensar(self, duracion=3):
      def animacion():
          self.label.config(image=self.image_pensando)
          self.root.update()
          time.sleep(duracion)
          self.label.config(image=self.image1)
          self.root.update()
          
      threading.Thread(target=animacion).start()

    def cerrar(self):
        if self.root:
            self.root.quit()   # Sale del mainloop
            self.root.destroy()  # Cierra la ventana

avatar_instance = AvatarApp()