class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        
    def imprimir(self):
        print("Datos de la persona:")
        print(self.nombre, "tiene una edad de", self.edad, "años.")
        
    def mayoríaEdad(self):
        if (self.edad>=18):
            print("Es mayor de edad")
        else:
            print("No es mayor de edad")

#Principal
nombre=input("Introduce el nombre de la persona")
edad=int(input("Introduce la edad de la persona"))
Persona1=Persona(nombre,edad)
Persona1.imprimir()
Persona1.mayoríaEdad()
