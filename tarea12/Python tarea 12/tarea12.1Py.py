#Función que crea una lista de N elementos
def crearlista():
    lista=[]
    N=int(input("¿Cuántos elementos tiene la lista?"))
    for x in range(N):
        V=int(input("Introduce un elemento de la lista"))
        lista.append(V)
    return lista
#Función que multiplica
def multiplicar(lista):
    for x in range(len(lista)):
        lista[x]=lista[x]*N
    print(lista)


#Programa principal
lista=crearlista()
print(lista)
N=int(input("Número a multiplicar"))
multiplicar(lista)
