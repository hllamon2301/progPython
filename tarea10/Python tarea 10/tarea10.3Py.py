Nombres=[]
Precios=[]
for x in range(5):
    N=input("Introduce el nombre del producto")
    Nombres.append(N)
    P=int(input("Introduce el precio del producto"))
    Precios.append(P)
print("El precio del primer producto",Nombres[0], "es", Precios[0])
print("Estos son los productos superiores al primero en cuanto a su precio")
for x in range(1,5):
    if Precios[x]>Precios[0]:
        print(Nombres[x]," ",Precios[x])
