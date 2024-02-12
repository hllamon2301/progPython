#Crear nuevo alumno
def Nuevo(lista):
    N=input("Introduce nombre y apellidos")
    Code=int(input("Introduce el código del alumno"))
    As=input("Introduce la asignatura cursada del alumno")
    C=float(input("introduce la nota del alumno en esta asignatura"))
    lista.append((Code,N,As,C))
    return lista
#Eliminar
def Eliminar(lista,code):
    ind=0
    estado=1
    while estado==1 and ind<len(lista):
        estudiante=lista[ind]
        if estudiante[0]==code:
            estado=0
        ind=ind+1
    if estado==0:
        lista.pop(ind-1)
    return lista
#Editar
def Edit(lista,code):
    ind=0
    estado=1
    while estado==1 and ind<len(lista):
        estudiante=lista[ind]
        if estudiante[0]==code:
             N=input("Introduce nombre y apellidos")
             As=input("Introduce la nueva asignatura cursada del alumno")
             C=float(input("introduce la nueva nota del alumno en esta asignatura"))
             estado=0
             ind=ind+1
        if estado==0:
            lista.pop(ind-1)
            lista.insert(ind-1,(code,N,As,C))
        return lista
#Mostrar
def Mostrar(lista):
    for alumno in lista:
        for datos in alumno:
            print(datos,end=" ")
        print()
#Mostrar por asignatura
def MostrarAs(lista,As):
    for alumno in lista:
        if alumno[2]==As:
            for datos in alumno:
                print(datos,end=" ")
        print()
    
#Mostrar aprobados por asignatura
def MostrarAprob(lista,As):
     for alumno in lista:
        if alumno[2]==As and alumno[3]>=5:
            for datos in alumno:
                print(datos,end=" ")
        print()
#Menú
def menu():
    print("________________________________________________")
    print("1, Agregar estudiante")
    print("________________________________________________")
    print("2, Eliminar estudiante")
    print("________________________________________________")
    print("3, Editar nuevo estudiante")
    print("________________________________________________")
    print("4, Mostrar estudiantes")
    print("________________________________________________")
    print("5, Mostrar estudiantes por asignatura")
    print("________________________________________________")
    print("6, Mostrar aprobados en asignatura")
    print("________________________________________________")
    print("7, salir")
    print("________________________________________________")
    opcion=int(input("Elige una opción"))
    return opcion
#Programa principal
opcion=0
lista=[]
while opcion!=7:
    opcion=menu()
    if opcion==1:
        lista=Nuevo(lista)
    if opcion==2:
        code=int(input("Introduce el código del estudiante a eliminar"))
        lista=Eliminar(lista,code)
    if opcion==3:
        code=int(input("Introduce el código del alumno a modificar"))
        lista=Edit(lista,code)
    if opcion==4:
        Mostrar(lista)
    if opcion==5:
        As=input("Asignatura a consultar")
        MostrarAs(lista,As)
    if opcion==6:
        As=input("Asignatura a consultar")
        MostrarAprob(lista,As)
