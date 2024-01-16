Al=[]
Nt=[]
for x in range(10):
    N=input("Introduce el nombre del alumno")
    Al.append(N)
    M=float(input("Introduce la nota del alumno"))
    Nt.append(M)
print("Alumnos aprobados")
for x in range(10):
    if Nt[x]>=5:
        print(Al[x]," ",Nt[x])
print("Alumnos suspensos")
for x in range(10):
    if Nt[x]<5:
        print(Al[x]," ",Nt[x])
