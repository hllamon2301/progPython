class operacion():

    def __init__(self):
        self.número1=int(input("Introduce un número"))
        self.número2=int(input("Introduce un número"))

    def suma(self):
        R=self.número1+self.número2
        print("La suma es", R)

    def resta(self):
        D=self.número1-self.número2
        print("La resta es", D)

    def prod(self):
        P=self.número1*self.número2
        print("El producto es", P)

    def div(self):
        C=self.número1/self.número2
        print("La división es", C)

#Principal
operacion=operacion()
operacion.suma()
operacion.resta()
operacion.prod()
operacion.div()
