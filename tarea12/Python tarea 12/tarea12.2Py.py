#Función que crea una lista de N elementos de caracteres
def crearlista():
    lista=[]
    N=int(input("¿Cuántos elementos tiene la lista?"))
    for x in range(N):
        V=input("Introduce un elemento de la lista")
        lista.append(V)
    return lista
#Función que devuelve la palabra con más caracteres de una lista
def mascaracteres(lista):
    palabra=lista[0]
    for x in range(1,len(lista)):
        if len(lista[x])>len(palabra):
            palabra=lista[x]
    return palabra


#Programa principal
palabras=crearlista()
print(palabras)
print("Palabra con mas caracteres:",mascaracteres(palabras))
