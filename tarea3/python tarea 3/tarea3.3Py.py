X=int(input("Introduce la coordenada X"))
Y=int(input("Introduce la coordenada Y"))
if X>0:
    if Y>0:
        print("Primer cuadrante")
    else:
        print("Cuarto cuadrante")
else:
    if Y>0:
        print("Segundo cuadrante")
    else:
        print("Tercer cuadrante")
