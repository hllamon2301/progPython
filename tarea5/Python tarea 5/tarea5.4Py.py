N=int(input("Introduce el número de triángulos"))
E=0
I=0
Q=0
for x in range (N):
    Lado1=float(input("Introduce un lado"))
    Lado2=float(input("Introduce un lado"))
    Lado3=float(input("Introduce un lado"))
    if Lado1==Lado2 and Lado1==Lado3:
        Q=Q+1
        print("Equilátero")
    else:
        if Lado1==Lado2 or Lado2==Lado3 or Lado1==Lado3:
            I=I+1
            print("Isósceles")
        else:
            E=E+1
            print("Escaleno")
print("Equiláteros", Q)
print("Isósceles", I)
print("Escalenos", E)
