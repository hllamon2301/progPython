#Clase triángulo con 3 propiedades, lado1, lado2 y lado3
class Triángulo:

    def __init__(self,l1,l2,l3):
        self.lado1=l1
        self.lado2=l2
        self.lado3=l3

    def Mayor(self):
        print("El lado mayor mide")
        if self.lado1>self.lado2 and self.lado1>self.lado3:
            print(self.lado1)
        else:
            if self.lado2>self.lado3:
                print(self.lado2)
            else:
                print(self.lado3)

    def Equilátero(self):
        if (self.lado1==self.lado2 and self.lado2==self.lado3):
            print("Este triángulo es equilátero")
        else:
            print("Este triángulo no es equilátero")

#Programa principal
l1=int(input("Lado 1"))
l2=int(input("Lado 2"))
l3=int(input("Lado 3"))
Triángulo1=Triángulo(l1,l2,l3)
Triángulo1.Mayor()
Triángulo1.Equilátero()
