import tkinter as tk
from tkinter import messagebox as mb
import sys
from math import sqrt

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.agregar_menu()
        self.agregar_componentes()
        self.ventana1.mainloop()

    def agregar_menu(self):
        self.menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=self.menubar1)
        self.opciones1 = tk.Menu(self.menubar1, tearoff=0)
        self.opciones1.add_command(label="Salir", command=self.salir)
        self.opciones1.add_command(label="Acerca de...", command=self.acerca)
        self.menubar1.add_cascade(label="Opciones", menu=self.opciones1)    
    def agregar_componentes(self):
        self.label1=tk.Label(self.ventana1, text="Ecuación de Segundo Grado")
        self.label1.grid(row=0, column=0)
        self.label2=tk.Label(self.ventana1, text="Ingrese el valor de 'A'")
        self.label2.grid(row=1, column=0)
        self.A=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width=20, textvariable=self.A)
        self.entry1.grid(row=1, column=1)
        self.label3=tk.Label(self.ventana1, text="Ingrese el valor de 'B'")
        self.label3.grid(row=2, column=0)
        self.B=tk.StringVar()
        self.entry2=tk.Entry(self.ventana1, width=20, textvariable=self.B)
        self.entry2.grid(row=2, column=1)
        self.label4=tk.Label(self.ventana1, text="Ingrese el valor de 'C'")
        self.label4.grid(row=3, column=0)
        self.C=tk.StringVar()
        self.entry3=tk.Entry(self.ventana1, width=20, textvariable=self.C)
        self.entry3.grid(row=3, column=1)

        self.button1=tk.Button(self.ventana1, text="Calcular", command=self.operar)
        self.button1.grid(row=4, column=1)
        
        
    def salir(self):
        respuesta=mb.askyesno("Atención", "¿Quiere salir del programa?")
        if respuesta==True:
            sys.exit()

    def acerca(self):
        mb.showinfo("Hugo Llamas Montes","Programa diseñado con intención didáctica del uso del programa python y tkinter.")

    def operar(self):
        if self.A.get()=="" or self.B.get()=="" or self.C.get()=="":
            mb.showerror("Cuidado", "Una de las variables debe estar sin rellenar, compruebe y confirme de nuevo.")
        else:
            A=int(self.A.get())
            B=int(self.B.get())
            C=int(self.C.get())
            
            R=B*B-4*A*C
            if R<0:
                mb.showerror("Irreal", "Esta ecuación no tiene solución en R")
            elif R==0:
                X=(-B)/(2*A)
                mb.showinfo("Una solución", "La única solución de esta ecuación es "+str(X))
            elif R>0:
                S=sqrt(R)
                X=(-B+S)/(2*A)
                Y=(-B-S)/(2*A)
                mb.showinfo("Dos soluciones", "Las soluciones de esta ecuación son "+str(X)+" y "+str(Y))
aplicacion1=Aplicacion() 
