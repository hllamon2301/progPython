#Función para crear nombre y sueldo de empleados
def Empleado():
    Nom=input("Introduce el nombre del empleado")
    Suel=int(input("Introduce el sueldo del empleado"))
    return (Nom,Suel)
#Devolver el mayor sueldo de dos empleados
def Mayor(Empl1,Empl2):
    if Empl1[1]>Empl2[1]:
        print("El sueldo mayor es de", Empl1[0], "con", Empl1[1])
    else:
        print("El sueldo mayor es de", Empl2[0], "con", Empl2[1])
#Programa principal
Empl1=Empleado()
Empl2=Empleado()
Mayor(Empl1,Empl2)
