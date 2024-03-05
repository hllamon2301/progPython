import tkinter as tk

class Aplicacion:
    def __init__(self):
        
        self.ventana1=tk.Tk()
        self.label1=tk.Label(self.ventana1,text="Usuario:")
        self.label1.grid(column=0, row=0)
        
        self.dato1=tk.StringVar()
        
        self.entry1=tk.Entry(self.ventana1, width=10, textvariable=self.dato1)
        self.entry1.grid(column=0, row=1)
        
        self.label2=tk.Label(self.ventana1,text="Contraseña:")
        self.label2.grid(column=2, row=0)
        
        self.dato2=tk.StringVar()
        
        self.entry2=tk.Entry(self.ventana1, width=10, textvariable=self.dato2, show="*")
        self.entry2.grid(column=2, row=1)
        
        self.boton1=tk.Button(self.ventana1, text="Enter", command=self.Enter)
        self.boton1.grid(column=1, row=2)
        
        self.label3=tk.Label(self.ventana1,text="")
        self.label3.grid(column=1, row=3)
        
        self.ventana1.mainloop()

    def Enter(self):
        valor1=self.dato1.get()
        valor2=self.dato2.get()
        if valor1=="Juan" and valor2=="abc123":
            self.label3.configure(text="Correcto")
        else:
            self.label3.configure(text="Acceso denegado")
            
        
Aplicación1=Aplicacion()
