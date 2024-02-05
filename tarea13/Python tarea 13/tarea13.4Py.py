#Leer una lista de 3 candidatos
def Candidatos():
    Candidatos=[]
    for x in range(3):
        Nom=input("El nombre del candidato")
        Prov=[]
        otraProv="si"
        while otraProv=="si":
            Provincia=input("Introduce el nombre de la provincia")
            Votos=int(input("Introduce el número de votos de la provincia"))
            Prov.append((Provincia,Votos))
            otraProv=input("¿Vas a introducir otra provincia?(si/no)")
        Candidatos.append((Nom,Prov))
    return Candidatos

#Visualizar votos
def Visualizar(Candidatos):
    for Candidato in Candidatos:
        total=0
        for Provincia in Candidato[1]:
            total=total+Provincia[1]
        print(Candidato[0], "ha obtenido un total de votos de", total)

#Programa principal
Candidatos=Candidatos()
Visualizar(Candidatos)
