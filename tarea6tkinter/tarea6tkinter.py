import tkinter as tk
from tkinter import ttk
import sys
class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        
        self.label1=ttk.Label(self.ventana1, text="Nombre:")
        self.label1.grid(column=0, row=0)
        
        self.label2=ttk.Label(self.ventana1, text="Nota:")
        self.label2.grid(column=0, row=1)
        
        self.dato1=tk.StringVar()
        self.entry1=ttk.Entry(self.ventana1, width=20, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0)
        
        self.dato2=tk.StringVar()
        self.entry2=ttk.Entry(self.ventana1, width=20, textvariable=self.dato2)
        self.entry2.grid(column=1, row=1)
        
        self.boton1=ttk.Button(self.ventana1, text="Insertar", command=self.Insert)
        self.boton1.grid(column=0, row=2)
        
        self.boton2=ttk.Button(self.ventana1, text="Eliminar", command=self.Elim)
        self.boton2.grid(column=1, row=2)
        
        self.menubar1=tk.Menu(self.ventana1)
        self.ventana1.config(menu=self.menubar1)
        opcion=tk.Menu(self.menubar1)
        opcion.add_command(label="Salir", command=self.Salir)
        self.menubar1.add_cascade(label="Opciones", menu=opcion)
        
        
        self.listbox=tk.Listbox(self.ventana1)
        self.listbox.grid(column=0, row=3, columnspan=2, sticky="we")
        
        self.ventana1.mainloop()



    def Insert(self):
        self.contador=0
        self.listbox.insert(self.contador,self.dato1.get()+"-"+self.dato2.get())
        self.contador=self.contador+1
    def Elim(self):
        if len(self.listbox1.curselection()!=0):
               item=self.listbox1.curselection()[0]
               self.listbox.delete(item)
               self.contador=self.contador-1

    def Salir(self):
        sys.exit()

        
aplicacion1=Aplicacion()


