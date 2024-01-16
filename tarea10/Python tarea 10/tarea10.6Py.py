lista1=[]
for x in range(10):
    N=int(input("Introduce un número"))
    lista1.append(N)
#Algoritmo de la burbuja para ordenar números
for i in range(1,10):
    for j in range(10-i):
        if lista1[j]>lista1[j+1]:
            aux=lista1[j]
            lista1[j]=lista1[j+1]
            lista1[j+1]=aux         
print("Lista ordenada", lista1)
