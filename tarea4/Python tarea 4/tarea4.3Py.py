n=int(input("¿Cuántos empleados hay?"))
Imp=0
M=0
Y=0
x=1
while x<=n:
    S=int(input("Introduce un sueldo"))
    if S>500 or S<100:
        print("El valor introducido es incorrecto")
    if S>=100 and S<=300:
        M=M+1
        x=x+1
        Imp=S+Imp
    if S>300 and S<=500:
        Y=Y+1
        x=x+1
        Imp=S+Imp
print("Cobran entre 100 y 300", M, "empleado/s")
print("Cobran más de 300", Y, "empleado/s")
print("El importe de gastos en personal es", Imp)
