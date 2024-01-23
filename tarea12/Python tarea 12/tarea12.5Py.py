#Crear las listas
def Crear(R):  
    N=[]
    P=[]
    for x in range(R):
        V=input("Introduce el nombre del producto")
        B=int(input("Introduce el precio del producto"))
        N.append(V)
        P.append(B)
    return [N,P]
#Visualizar artículos y precios
def Ver(N,P):
    for x in range(len(N)):
        print(N[x],":",P[x])
#Artículo de mayor precio
def Mayor(N,P):
    G=P[0]
    pos=0
    for x in range(1,len(P)):
        if P[x]>G:
            G=P[x]
            pos=x
    print("El artículo más caro es:", N[pos], "a", G, "euros")
#Posibilidad de compra
def Compra(N,P):
    C=int(input("¿Cuál es el importe a comparar?"))
    for x in range(len(P)):
          if P[x]<=C:
              print(N[x], "es un precio menor o igual al dado")
#Programa principal
R=int(input("¿Cuántos artículos hay?"))
N,P=Crear(R)
Ver(N,P)
Mayor(N,P)
Compra(N,P)
