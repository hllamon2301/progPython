#Creamos una lista de los sueldos de N empleados
def crearLista(N):
    lista=[]
    for x in range(N):
        V=int(input("Introduce un sueldo"))
        lista.append(V)
    return lista
#Visualización de sueldos
def Ver(lista):
    print(lista)
#Sueldo superior a 4000
def Superior(lista):
    C=0
    for x in range(len(lista)):
        if lista[x]>4000:
            C=C+1
    print(C, "sueldos son superiores a 4000")
#Sueldo medio
def Medio(lista):
    S=0
    for x in range(len(lista)):
        S=S+lista[x]
    M=S/len(lista)
    return M
#Sueldos bajo el promedio
def Inferior(lista):
    M=Medio(lista)
    print("Los sueldos por debajo de la media son:")
    for x in range(len(lista)):
        if lista[x]<M:
            print(lista[x])
#Programa principal
N=int(input("¿Cuántos empleados hay?"))
lista=crearLista(N)
Ver(lista)
Superior(lista)
print("El sueldo medio es", Medio(lista))
Inferior(lista)
