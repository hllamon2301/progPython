#Crear lista de palabras [("Hola",4),("Patata",6)...]
def lista(n):
    Lista=[]
    for x in range(n):
        P=input("Introduce una palabra")
        long=len(P)
        Lista.append((P,long))
    return Lista

#Visualizar palabras mayores de 5 carácteres
def Visualizar(Lista):
    for palabra in Lista:
        if palabra[1]>5:
            print(palabra[0])
            
#Programa principal
n=int(input("¿Cuántas palabras vas a introducir?"))
Lista=lista(n)
Visualizar(Lista)
