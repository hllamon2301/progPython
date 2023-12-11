#El ordenador piensa un número y debes acertarlo en menos de 10 intentos
from random import randint
N=randint(1,100)
#Variable de control
C=0
#Almacenamos el número de intentos
I=0
while I<10 and C==0:
    M=int(input("Número"))
    I=I+1
    if M<N:
        print("Más grande")
    if N<M:
        print("Más pequeño")
    if N==M:
        print("Has acertado en", I, "intentos")
        C=1
if C==0:
    print("No has acertado")
