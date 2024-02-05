#Carga de lista con producto y precio [(Producto1,Precio1)...]
def Carga():
    Lista=[]
    for x in range(5):
        Prod=input("Introduce el nombre del producto")
        Prec=int(input("Introduce el precio de dicho producto"))
        Lista.append((Prod,Prec))
    return Lista

#Visualización
def Visualizar(Lista):
    for Valor in Lista:
        print("El precio del producto" ,Valor[0], "es de", Valor[1], "euros")

#Impresión de productos entre 10 y 15 euros
def Entre10y15(Lista):
    print("Los productos cuyo precio se halla entre 10 y 15 euros son:")
    for Valor in Lista:
        if Valor[1]>=10 and Valor[1]<=15:
            print(Valor[0])

#Programa principal
Lista=Carga()
Visualizar(Lista)     
Entre10y15(Lista)
