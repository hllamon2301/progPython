N=int(input("Introduce cuántos triángulos se van a leer"))
M=0
for x in range(N):
    B=float(input("Base del triángulo"))
    H=float(input("Altura del triángulo"))
    S=(B*H)/2
    print("El triángulo con base", B, "y altura", H, "tiene de superficie", S)
    if S>12:
        M=M+1
print(M, "triángulos tienen una superficie mayor a 12")
