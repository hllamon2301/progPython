lista=[]
S=0
for x in range(5):
    H=float(input("Introduce una altura"))
    lista.append(H)
    S=S+lista[x]
M=S/5
print("La altura media es", M)
C=0
c=0
for x in range(5):
    if lista[x]>M:
        C=C+1
    else:
        c=c+1
print(C, "alturas superan a la media, y", c, "alturas son menores que la media")
        
