O=input("Ingrese una oración")
x=0
V=0
F=O.lower()
while x<len(F):
    if F[x]=="a" or F[x]=="e" or F[x]=="i" or F[x]=="o" or F[x]=="u":
        V=V+1
    x=x+1
print("Hay", V, "vocales")
