"""
Realizar un programa que solicite la carga de valores enteros por teclado y los sume. Finalizar la carga al ingresar el valor -1.
Dejar como comentario dentro del código fuente el enunciado del problema.
"""
N=0
S=0
while N!=-1:
    N=int(input("Introduce un número"))
    if N!=-1:
        S=S+N
if N==-1:
    print("La suma es igual a ", S)
