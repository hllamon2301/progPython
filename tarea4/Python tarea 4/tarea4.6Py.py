L1=1
L2=1
S1=0
S2=0
while L1<=5:
     M=int(input("Introduce valores de la lista 1"))
     S1=S1+M
     L1=L1+1
while L2<=5:
     N=int(input("Introduce valores de la lista 2"))
     S2=S2+N
     L2=L2+1
if S1>S2:
    print("La lista 1 es mayor")
if S2>S1:
    print("La lista 2 es mayor")
if S2==S1:
    print("Las listas son iguales")
    
    
