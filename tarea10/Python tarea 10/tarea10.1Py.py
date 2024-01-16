#Definimos las listas vacías
Nombres=[]
Sueldos=[]
#Agregamos 5 nombres y sueldos
for x in range(5):
    N=input("Introduce un nombre")
    Nombres.append(N)
    S=int(input("Introduce el sueldo de dicha persona"))
    Sueldos.append(S)
#Visualizar la persona con mayor y menor sueldo
May=0
Men=99999999999999999999999999999
posMy=0
posMn=0
for x in range(5):
    if Sueldos[x]>May:
        May=Sueldos[x]
        posMy=x
    if Sueldos[x]<Men:
        Men=Sueldos[x]
        posMn=x
print("El sueldo mayor es", May, "pertenece a", Nombres[posMy])
print("El sueldo menor es", Men, "pertenece a", Nombres[posMn])
