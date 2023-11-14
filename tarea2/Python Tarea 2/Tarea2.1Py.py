N=int(input("Introduce el primer número"))
M=int(input("Introduce el segundo número"))
if N>M:
    S=N+M
    R=N-M
    print("La suma es", S, "y la resta es", R)
else:
    P=N*M
    D=N/M
    print("El producto es", P, "y la división es", D)
    
