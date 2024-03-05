import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.dato=""
        self.label1=tk.Label(self.ventana1,text="Pulse cuantos botones desee")
        self.label1.grid(column=0, row=0)
        
        self.boton1=tk.Button(self.ventana1,text="1",command=self.Añadir1)
        self.boton1.grid(column=1,row=0)
        
        self.boton2=tk.Button(self.ventana1,text="2",command=self.Añadir2)
        self.boton2.grid(column=2,row=0)

        self.boton3=tk.Button(self.ventana1,text="3",command=self.Añadir3)
        self.boton3.grid(column=3,row=0)

        self.boton4=tk.Button(self.ventana1,text="4",command=self.Añadir4)
        self.boton4.grid(column=4,row=0)

        self.boton5=tk.Button(self.ventana1,text="5",command=self.Añadir5)
        self.boton5.grid(column=5,row=0)

        self.label2=tk.Label(self.ventana1,text="")
        self.label2.grid(column=0,row=2)

        self.ventana1.mainloop()
        
    def Añadir1(self):
        self.dato=self.dato+"-1"
        self.label2.configure(text=self.dato)
    def Añadir2(self):
        self.dato=self.dato+"-2"
        self.label2.configure(text=self.dato)

    def Añadir3(self):
        self.dato=self.dato+"-3"
        self.label2.configure(text=self.dato)

    def Añadir4(self):
        self.dato=self.dato+"-4"
        self.label2.configure(text=self.dato)

    def Añadir5(self):
        self.dato=self.dato+"-5"
        self.label2.configure(text=self.dato)
        
#Programa Principal
aplicacion1=Aplicacion()       
