Alumnos=[]
Notas=[]
for x in range(4):
    Al=input("Introduce el nombre del alumno")
    Alumnos.append(Al)
    Nt=float(input("Introduce la nota del alumno"))
    Notas.append(Nt)
MB=0
for x in range(4):
    if Notas[x]<4:
        print(Alumnos[x], "insuficiente")
    else:
        if Notas[x]<=7:
            print(Alumnos[x], "bueno")
        else:
            print(Alumnos[x], "muy bueno")
            MB=MB+1
print(MB, "alumnos han sido calificados como muy buenos")
    
