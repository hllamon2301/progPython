#Crear una cuenta
def Crear(Cantidad):
    S=Cantidad
    return S
#Consultar saldo
def Consulta(S):
    print("Su saldo actual es", S)
#Ingresar cantidad
def Ingresar(S,Cantidad):
    S=S+Cantidad
    return S
#Retirar cantidad
def Retirar(S,Cantidad):
    if Cantidad>S:
        print("No tiene saldo suficiente")
    else:
        S=S-Cantidad
    return S
#Menú
def menu(S):
    op=5
    while op!=4:
        print("1. Ingresar saldo")
        print("2. Retirar saldo")
        print("3. Consultar saldo")
        print("4. Salir")
        op=int(input("Introduce una opción"))
        if op==1:
            Cantidad=int(input("¿Qué cantidad quieres ingresar?"))
            S=Ingresar(S,Cantidad)
        if op==2:
            Cantidad=int(input("¿Qué cantidad quieres retirar?"))
            S=Retirar(S,Cantidad)
        if op==3:
            Consulta(S)
        if op==4:
            print("Gracias por su visita")

#Programa principal
S=int(input("Saldo inicial para crear la cuenta"))
menu(S)
        
