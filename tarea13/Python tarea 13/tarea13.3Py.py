#Crear lista con sublistas
def Empleados():
    Lista=[]
    for x in range(5):
        Nom=input("introduce el nombre del empleado")
        S1=int(input("Introduce el primer sueldo"))
        S2=int(input("Introduce el segundo sueldo"))
        S3=int(input("Introduce el tercer sueldo"))
        Empleado=(Nom,S1,S2,S3)
        Lista.append(Empleado)
    return Lista
#Carga empleados y su sueldo total
def Carga(Lista):
    for Empleado in Lista:
        total=Empleado[1]+Empleado[2]+Empleado[3]
        print(Empleado[0], "tiene un sueldo trimestral de", total)

#Empleados con monto trimestral mayor a 10000
def CargaSup(Lista):
    print("Los empleados con monto trimestral mayor a 10000 son:")
    for Empleado in Lista:
        total=Empleado[1]+Empleado[2]+Empleado[3]
        if total>10000:
            print(Empleado[0], "tiene un sueldo trimestral de", total)
#Programa principal
Lista=Empleados()
Carga(Lista)
CargaSup(Lista)
