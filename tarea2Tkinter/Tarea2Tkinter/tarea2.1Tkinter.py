import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()

        self.seleccion=tk.IntVar()
        
      
        self.radio1=tk.Radiobutton(self.ventana1,text="Rojo", variable=self.seleccion, value=1)
        self.radio1.grid(column=0, row=0)
        
       
        self.radio2=tk.Radiobutton(self.ventana1,text="Azul", variable=self.seleccion, value=2)
        self.radio2.grid(column=0, row=1)

        self.radio3=tk.Radiobutton(self.ventana1,text="Verde", variable=self.seleccion, value=3)
        self.radio3.grid(column=0, row=2)
      
        self.boton1=tk.Button(self.ventana1, text="Cambiar color", command=self.mostrarseleccionado)
        self.boton1.grid(column=1, row=1)

        
        self.label1=tk.Label(self.ventana1,text="Color")
        self.label1.grid(column=1, row=2)

        
        self.ventana1.mainloop()
        
    def mostrarseleccionado(self):
        if self.seleccion.get()==1:
            self.label1.configure(text="Rojo")
            self.ventana1.configure(bg="Red")
        if self.seleccion.get()==2:
            self.label1.configure(text="Azul")
            self.ventana1.configure(bg="Blue")
        if self.seleccion.get()==3:
            self.label1.configure(text="Verde")
            self.ventana1.configure(bg="Green")

aplicacion1=Aplicacion() 

