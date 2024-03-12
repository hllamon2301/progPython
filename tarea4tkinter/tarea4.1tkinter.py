import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.pais=tk.StringVar()
        pais=("España","Alemania","Italia","Portugal","Francia","UK","Suiza")
        self.combobox1=ttk.Combobox(self.ventana1, width=10, textvariable=self.pais, values=pais)
        self.combobox1.current(0)
        self.combobox1.grid(column=2, row=2)
        self.boton1=tk.Button(self.ventana1, text="Confirmar", command=self.recuperar)
        self.boton1.grid(column=1, row=2)
        self.label1=tk.Label(self.ventana1,text="Seleccionado:")
        self.label1.grid(column=1, row=3)
        self.dato1=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width=20, textvariable=self.dato1)
        self.entry1.grid(column=2, row=1)
        self.label2=tk.Label(self.ventana1, text="[]")
        self.label2.grid(column=1, row=4)
        self.ventana1.mainloop()

    def recuperar(self):
            self.label2.configure(text=self.dato1.get()+", "+self.pais.get())

aplicacion1=Aplicacion()         
