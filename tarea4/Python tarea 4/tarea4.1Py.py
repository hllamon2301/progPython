X=1
Aprobado=0
Suspenso=0
while X<=10:
    N=int(input("Introduce una nota"))
    X=X+1
    if N>=5:
        Aprobado=Aprobado+1
    else:
        Suspenso=Suspenso+1
print("Han aprobado", Aprobado, "y han suspendido", Suspenso)
