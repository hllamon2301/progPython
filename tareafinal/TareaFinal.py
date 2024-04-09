import tkinter as tk
from tkinter import scrolledtext as st
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as mb

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.agregarcomponentes()
        self.Menú()
        self.ventana1.mainloop()
    def agregarcomponentes(self):
        self.label1=tk.Label(self.ventana1, text="Código")
        self.label1.grid(row=1, column=0)
        self.label2=tk.Label(self.ventana1, text="Nombre")
        self.label2.grid(row=1, column=1)
        self.label3=tk.Label(self.ventana1, text="Apellidos")
        self.label3.grid(row=1, column=2)
        self.label4=tk.Label(self.ventana1, text="Nota")
        self.label4.grid(row=1, column=3)
        self.label5=tk.Label(self.ventana1, text="Aprobados")
        self.label5.grid(row=3, column=1)
        self.label6=tk.Label(self.ventana1, text="Suspensos")
        self.label6.grid(row=3, column=2)

        self.Code=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width=20, textvariable=self.Code)
        self.entry1.grid(row=2, column=0)
        self.Name=tk.StringVar()
        self.entry2=tk.Entry(self.ventana1, width=20, textvariable=self.Name)
        self.entry2.grid(row=2, column=1)
        self.Sur=tk.StringVar()
        self.entry3=tk.Entry(self.ventana1, width=20, textvariable=self.Sur)
        self.entry3.grid(row=2, column=2)
        self.Nota=tk.StringVar()
        self.entry4=tk.Entry(self.ventana1, width=20, textvariable=self.Nota)
        self.entry4.grid(row=2, column=3)

        self.button1=tk.Button(self.ventana1, text="Confirmar", command=self.Confirmar)
        self.button1.grid(row=0, column=0)
        

        self.listbox1=tk.Listbox(self.ventana1)
        self.listbox1.grid(column=1,row=4)
        self.listbox2=tk.Listbox(self.ventana1)
        self.listbox2.grid(column=2,row=4)

    def Menú(self):
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1 = tk.Menu(menubar1)
        opciones1.add_command(label="Guardar", command=self.Guarda)
        opciones1.add_command(label="Salir", command=self.Salir)
        menubar1.add_cascade(label="Opciones", menu=opciones1)   
        
        
        
        
        

    def Confirmar(self):
        C=0
        V=0
        Alumnos=[]
        if self.Code.get()=="" or self.Name.get()=="" or self.Sur.get()=="" or self.Nota.get()=="":
            mb.showerror("Error", "Alguno de los parámetros debe estar vacío. Compruebe y pruebe otra vez")
        else:
            Alumno=(self.Code.get(),":",self.Name.get(),self.Sur.get(),float(self.Nota.get()))
            Alumnos.append(Alumno)
            if Alumno[4]>=5:
                self.listbox1.insert(C,Alumno)
                C=C+1
            else:
                
                self.listbox2.insert(V,Alumno)
                V=V+1
        return Alumnos
    def Salir(self):
        sys.exit()
        
    def Guarda(self):
        archi1=open("datos.txt","w")
        archi1.write(self.Code.get()+self.Name.get()+self.Sur.get()+self.Nota.get())
        archi1.close
        mb.showinfo("Guardar", "Se ha guardado con éxito el archivo.")
        



            
      
aplicacion1=Aplicacion() 
