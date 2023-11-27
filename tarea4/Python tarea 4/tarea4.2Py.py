n=int(input("Introduce el número de personas"))
X=1
Sum=0
while X<=n:
    A=float(input("Introduce una altura"))
    Sum=Sum+A
    X=X+1
Prom=Sum/n
print("La altura promedio es", Prom)
    
