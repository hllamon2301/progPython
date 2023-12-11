"""
Realizar la carga de dos nombres de personas distintos. Mostrar por pantalla luego ordenados en forma alfabética
"""
#Introducir los nombres
N1=input("Introduce un nombre")
N2=input("Introduce otro nombre")
if N1==N2:
    print("Has introducido el mismo nombre")
if N1>N2:
    print(N2, "", N1)
else:
    print(N1, "", N2)
