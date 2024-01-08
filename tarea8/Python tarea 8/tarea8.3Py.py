x=0
while x==0:
    C=input("Introduce una clave")
    if len(C)<10 or len(C)>20:
        print("Clave incorrecta")
    else:
        print("Clave aceptada")
        x=1
