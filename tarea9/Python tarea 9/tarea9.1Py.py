#Definir una lista vacía
lista=[]
#Se agregan 8 elementos
for x in range(8):
    V=int(input("Ingresa un número"))
    lista.append(V)
#Calculamos cuántos números son >100
C=0
for x in range(8):
    if lista[x]>100:
        C=C+1
#Visualizamos datos
print(lista)
print(C, "números son mayores que 100")
        

    
