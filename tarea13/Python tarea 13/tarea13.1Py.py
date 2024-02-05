#Función que crea una lista de 5 enteros
def Crearlista():
    L=[]
    for x in range(5):
        N=int(input("Ingrese un entero"))
        L.append(N)
    return L

#Devolver mayor y menor
def May(L):
    Y=L[0]
    M=L[0]
    for N in L:
        if N>Y:
            Y=N
        if N<M:
            M=N
    return (Y,M)
        



#Programa principal
L=Crearlista()
MM=May(L)
print("La nota más alta es", MM[0])
print("La nota más baja es", MM[1])
