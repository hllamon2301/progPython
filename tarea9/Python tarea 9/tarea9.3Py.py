lista=[]
for x in range(5):
    N=input("Ingrese un nombre")
    lista.append(N)
#Visualizar cuántos tienen 5 o más caracteres
for x in range(5):
    if len(lista[x])>=5:
        print(lista[x], end=" ")
        
