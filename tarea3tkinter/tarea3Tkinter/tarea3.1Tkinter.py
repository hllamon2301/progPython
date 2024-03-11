import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.seleccion=tk.IntVar()
        self.check1=tk.Checkbutton(self.ventana1,text="Google", variable=self.seleccion)
        self.check1.grid(column=0, row=0)
        self.seleccion2=tk.IntVar()
        self.check2=tk.Checkbutton(self.ventana1,text="Opera", variable=self.seleccion2)
        self.check2.grid(column=0, row=1)
        self.seleccion3=tk.IntVar()
        self.check3=tk.Checkbutton(self.ventana1, text="Firefox", variable=self.seleccion3)
        self.check3.grid(column=0, row=2)
        self.seleccion4=tk.IntVar()
        self.check4=tk.Checkbutton(self.ventana1, text="Edge", variable=self.seleccion4)
        self.check4.grid(column=0, row=3)
        self.boton1=tk.Button(self.ventana1, text="Confirmar", command=self.activar)
        self.boton1.grid(column=1, row=1)
        self.label1=tk.Label(self.ventana1, text="Navegadores")
        self.label1.grid(column=1, row=2)
        self.ventana1.mainloop()
    def activar(self):
        nav=""
        if self.seleccion.get()==1:
            nav+="\nGoogle"
        if self.seleccion2.get()==1:
            nav+="\nOpera"
        if self.seleccion3.get()==1:
            nav+="\nFirefox"
        if self.seleccion4.get()==1:
            nav+="\nEdge"
        self.label1.configure(text="Navegadores:"+str(nav))   
            
aplicacion1=Aplicacion()         
