O=input("Ingrese una oración")
x=0
C=0
while x<len(O):
    if O[x]==" ":
        C=C+1
    x=x+1
print("En esta oración hay", C+1, "palabras")
