N=int(input("Introduce cuántos valores vas a introducir"))
I=0
P=0
M=1
while M<=N:
    V=int(input("Introduce un valor"))
    M=M+1
    if V%2==0:
        P=P+1
    else:
        I=I+1
print(P, "valores son pares y", I, "valores son impares.")
