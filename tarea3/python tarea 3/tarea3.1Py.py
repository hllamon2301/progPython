N=int(input("Introduce un número:"))
V=int(input("Introduce un número:"))
M=int(input("Introduce un número:"))
if N>V and N>M:
    print("El mayor es", N)
else:
    if V>M:
        print("El mayor es", V)
    else:
        print("El mayor es", M)
if N<V and N<M:
    print("El menor es", N)
else:
    if V<M:
        print("El menor es", V)
    else:
        print("El menor es", M)
