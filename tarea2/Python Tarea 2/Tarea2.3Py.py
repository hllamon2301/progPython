N=int(input("Introduce un número de uno o dos dígitos"))
if N>0:
    if N<100:
        if N>=10:
             print("El número tiene dos cifras")
        else:
             print("El número tiene una cifra")
    else:
        print("El número tiene más de dos cifras")
else:
    print("El número es negativo")
