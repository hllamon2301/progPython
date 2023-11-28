PM=0
PT=0
PN=0
for x in range (5):
    EM=int(input("Introduce edades del turno de mañana"))
    PM=PM+EM
for x in range (6):
    ET=int(input("Introduce edades del turno de tarde"))
    PT=PT+ET
for x in range (11):
    EN=int(input("Introduce edades del turno de noche"))
    PN=PN+EN
PN=PN/11
PT=PT/6
PM=PM/5
print("Promedio del turno de mañana", PM)
print("Promedio del turno de tarde", PT)
print("Promedio del turno de noche", PN)
if PM>PT:
    if PM>PN:
        print("El promedio mayor es el del turno de mañana")
    if PN>PM:
        print("El promedio mayor es el del turno de noche")
else:
    if PT>PN:
        print("El promedio mayor es el del turno de tarde")
    if PT<PN:
        print("El promedio mayor es el del turno de noche")

    
