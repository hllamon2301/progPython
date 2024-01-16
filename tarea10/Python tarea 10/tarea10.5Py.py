L1=[]
L2=[]
L3=[]
for x in range(4):
    N1=int(input("Introduce un número"))
    L1.append(N1)
    N2=int(input("Introduce el número a sumar"))
    L2.append(N2)
for x in range(4):
    N3=L1[x]+L2[x]
    L3.append(N3)
print("La lista resultante:", L3)
    
