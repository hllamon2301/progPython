class Jugador:
    juego=30

    def __init__(self):
        self.nombre=input("Introduce el nombre")
        self.puntos=int(input("Introducir puntos"))

    def imprimir(self):
        print(self.nombre, "tiene", self.puntos, "puntos")
        print("Quedan", Jugador.juego, "minutos")

    def time(self):
        Jugador.juego=Jugador.juego-1


#Principal
Jugador1=Jugador()
Jugador2=Jugador()
for x in range(10):
    Jugador1.time()
Jugador1.imprimir
while Jugador.juego>0:
    Jugador2.imprimir()
    Jugador2.time()
