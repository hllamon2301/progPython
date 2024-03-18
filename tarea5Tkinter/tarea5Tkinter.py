import tkinter as tk
from tkinter import ttk
import sys

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        label1=tk.Label(self.ventana1, text="Ancho")
        label1.grid(column=1, row=0)
        self.dato1=tk.StringVar()
        entry1=tk.Entry(self.ventana1, width=20, textvariable=self.dato1)
        entry1.grid(column=1, row=1)
        label2=tk.Label(self.ventana1, text="Largo")
        label2.grid(column=2, row=0)
        self.dato2=tk.StringVar()
        entry2=tk.Entry(self.ventana1, width=20, textvariable=self.dato2)
        entry2.grid(column=2, row=1)
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1 = tk.Menu(menubar1)
        opciones1.add_command(label="Confirmar", command=self.Tamaño)
        opciones1.add_separator()
        opciones1.add_command(label="Salir", command=self.Salir)
        menubar1.add_cascade(label="Aplicar", menu=opciones1)        
        self.ventana1.mainloop()

    def Tamaño(self):
        self.ventana1.geometry(self.dato1.get()+"x"+self.dato2.get())
        
    def Salir(self):
        sys.exit()
        
aplicacion1=Aplicacion()
