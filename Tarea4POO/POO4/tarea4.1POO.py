#Clase Cuenta con nombre de titular y monto
class Cuenta:
    def __init__(self):
       self.nombre=input("Introduce nombre")
       self.monto=int(input("Introduce monto"))


#Visualizar cuenta
    def Print(self):
        print(self.nombre, "tiene un monto de", self.monto)
#Clase CajaAhorro
class CajaAhorro(Cuenta):
    def __init__(self):
        super().__init__()


#Visualizar datos de CajaAhorro
    def imprimir(self):
        super().Print()

#Clase PlazoFijo que dispone de intereses y plazo de imposición
class PlazoFijo(Cuenta):
    def __init__(self):
        super().__init__()
        self.interes=float(input("Intereses"))
        self.imposición=int(input("Plazo de imposición"))
        
#Visualizar datos de la clase PlazoFijo
    def imprimir(self):
        super().Print()
        print("Intereses",self.interes)
        print("Plazo de imposición",self.imposición)

#Visualizar ganancia
    def ganancia(self):
        ganancia=self.monto*self.interes/100
        print("Ganancia", ganancia)


#Programa principal
caja=CajaAhorro()
caja.Print()

plazo=PlazoFijo()
plazo.imprimir()
plazo.ganancia()
