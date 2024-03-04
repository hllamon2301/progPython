class Jugador():


    def __init__(self):
        self.nombre=input("Introduce el nombre")
        self.puntaje=int(input("Introduce puntos"))

    def __str__(self):
        cadena=self.nombre+"tiene un puntaje de "+str(self.puntaje)
        if self.puntaje>1000:
            cadena=cadena+" es experto"
        else:
            cadena=cadena+" es principiante"
        return cadena


#Principal
Jugador1=Jugador()
Jugador2=Jugador()
print(Jugador1)
print(Jugador2)
