N=int(input("Introduce la nota"))
if N<5:
    print("Has suspendido")
else:
    print("Has aprobado")
    if N<=6:
        print("Bien")
    if N>6 and N<9:
        print("Notable")
    if N>=9 and N<=10:
        print("Sobresaliente")
    
