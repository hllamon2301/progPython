from math import sqrt
A=int(input("Introduce la A"))
B=int(input("Introduce la B"))
C=int(input("Introduce la C"))
aux=B*B-4*A*C
if aux<0:
    print("Solución compleja")
else:
    R=sqrt(aux)
    X1=(-B+R)/2*A
    X2=(-B-R)/2*A
    print("Las soluciones son", X1, "y", X2)
