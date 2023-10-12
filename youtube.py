from pytube import YouTube
from tkinter import *
from tkinter import messagebox as MessageBox

def accion():
    enlace = videos.get()
    video = YouTube(enlace)
    descarga = video.streams.get_highest_resolution()
    descarga.download()

root = Tk()
root.config(bd=15)
root.title("Descargar videos de Youtube")

instruccion = Label(root, text="Ingrese la URL del video", fg="blue", font=("Arial", 12))
instruccion.grid(row=0, column=1)

videos = Entry(root, width=30)
videos.grid(row=1, column=1, padx=10, pady=10)

boton = Button(root, text="Descargar", command=accion)
boton.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()