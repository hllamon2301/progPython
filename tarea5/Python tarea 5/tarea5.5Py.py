L=int(input("¿Cuántos puntos se van a ingresar?"))
P=0
S=0
T=0
C=0
for v in range (L):
    x=float(input("Introduce la coordenada x"))
    y=float(input("Introduce la coordenada y"))
    if x>0:
        if y>0:
            P=P+1
            print("Primer cuadrante")
        if y<0:
            C=C+1
            print("Cuarto cuadrante")
    if x<0:
        if y<0:
            T=T+1
            print("Tercer cuadrante")
        if y>0:
            S=S+1
            print("Segundo cuadrante")
print("Primer cuadrante", P)
print("Segundo cuadrante", S)
print("Tercer cuadrante", T)
print("Cuarto cuadrante", C)

