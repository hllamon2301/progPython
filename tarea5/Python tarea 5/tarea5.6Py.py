N=0
P=0
M=0
S=0
for x in range (10):
    V=int(input("Introduce un número"))
    if V>0:
        P=P+1
    if V<0:
        N=N+1
    if V%15==0:
        M=M+1
    if V%2==0:
        S=S+V
print("Negativos", N)
print("Positivos", P)
print("Múltiplos de quince", M)
print("Suma de pares", S)
