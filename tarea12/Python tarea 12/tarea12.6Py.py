#Crear una lista
def Crear(N):
    lista=[]
    for x in range(N):
        V=int(input("Introduce un valor de la lista inicial"))
        lista.append(V)
    return lista

#División en dos listas
def Separar(lista):
    N=[]
    P=[]
    for x in range(len(lista)):
        if lista[x]>=0:
            P.append(lista[x])
        else:
            N.append(lista[x])
    print("Los positivos son:", P, "y los negativos son:", N)

#Programa principal
N=int(input("¿Cuántos elementos tiene la lista inicial?"))
lista=Crear(N)
Separar(lista)
    
