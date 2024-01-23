#Función que crea una lista de N elementos
def crearLista():
    lista=[]
    N=int(input("¿Cuántos elementos tiene la lista?"))
    for x in range(N):
        V=int(input("Introduce un elemento de la lista"))
        lista.append(V)
    return lista
#Función que devuelve el producto de sus elementos
def producto(lista):
    p=1
    for x in range(len(lista)):
        p=p*lista[x]
    return p

#Programa principal
lista=crearLista()
print(lista)
print("El producto de sus elementos es:", producto(lista))
