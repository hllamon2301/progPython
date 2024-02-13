#Clase Agenda con una lista con sublista
class Agenda():
    def __init__(self):
        self.lista=[]
    
#Carga de contacto
    def Carga(self):
        Nom=input("Nombre del contacto")
        Tel=int(input("Teléfono del contacto"))
        Mail=input("Correo del contacto")
        Contacto=[]
        Contacto.append(Nom)
        Contacto.append(Tel)
        Contacto.append(Mail)
        self.lista.append(Contacto)

#Listado de agenda
    def Mostrar(self):
        for Contacto in self.lista:
            print(Contacto[0],":",Contacto[1],"-",Contacto[2])

#Buscar contacto
    def Buscador(self):
        Nom=input("Buscar:")
        Enc=0
        long=len(self.lista)
        ind=0
        while Enc==0 and ind<long:
            if self.lista[ind][0]==Nom:
                print("Teléfono:",self.lista[ind][1], "correo:", self.lista[ind][2])
                Enc=1
            ind=ind+1
        if Enc==0:
            print("Este nombre no está en sus contactos")
        else:
            return ind-1

#Editar contacto
    def Editar(self):
        pos=self.Buscador()
        Tel=int(input("Introduce el nuevo teléfono"))
        Mail=input("Introduce el nuevo correo")
        self.lista[pos][1]=Tel
        self.lista[pos][2]=Mail
        
#Menú
    def Menu(self):
        opcion=0
        while opcion!=5:
            print("_____________________________")
            print("1.Crear nuevo contacto")
            print("_____________________________")
            print("2.Listar contactos")
            print("_____________________________")
            print("3.Buscar contacto")
            print("_____________________________")
            print("4.Modificar contacto")
            print("_____________________________")
            print("5.Finalizar programas")
            print("_____________________________")
            opcion=int(input("Eliga una opción"))
            if opcion==1:
                self.Carga()
            if opcion==2:
                self.Mostrar()
            if opcion==3:
                self.Buscador()
            if opcion==4:
                self.Editar()

#Principal
Agenda=Agenda()
Agenda.Menu()
