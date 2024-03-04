#Clase socio
class Socio:
    def __init__(self):
        self.nombre=input("Introduce el nombre del socio")
        self.anti=int(input("Introduce la edad de la suscripción del socio en años"))

        
    def imprimir(self):
        for socio in self.socios:
            print(self.nombre, "tiene una antigüedad de", self.anti)
       

    def verAnti(self):
        return self.anti

    def verNom(self):
        return self.nombre
    

   
    
    
#Clase club
class Club:
    def __init__(self):
        self.socios=[]
        

    def Añadir(self):
        socio=Socio()
        self.socios.append(socio)

    def MostrarTodos(self):
        for socio in self.socios:
            Socio.imprimir(self)
            
    def MostrarUno(self):
        pos=int(input("Introduce la posición del socio a visualizar"))
        if(pos<len(self.socios)):
            self.socios[pos].imprimir()

    def mostrarMay(self):
        mayor=self.socios[0]
        for socio in self.socios:
            if socio.verAnti()>mayor.verAnti():
                mayor=socio
        print(mayor, "es el socio con mayor antigüedad")
        
        


#Programa Principal
club=Club()
socio1=club.Añadir()
socio2=club.Añadir()
socio3=club.Añadir()
club.MostrarTodos()
club.MostrarUno()
club.mostrarMay()
