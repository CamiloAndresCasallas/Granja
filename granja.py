from bovino import Bovino
from animal import animal
from perro import Perro

class granja:
    def __init__(self):
        self.miperro=[]
        self.mibovino=[]
    
    def agregar_perro(self,edad,peso,raza,propietario,fecha_vacunacion):

        if len(self.miperro)==0:
            perro=Perro()
            self.edad=edad
            self.peso=peso
            self.raza=raza
            self.propietaro=propietario
            self.fecha_vacunacion=fecha_vacunacion

        else:
            pass


    def agregar_bovino(self,edad,peso,raza,propietario,fecha_vacunacion):

        if len(self.mibovino)==0:
            bovino=Bovino()
            self.edad=edad
            self.peso=peso
            self.raza=raza
            self.propietaro=propietario
            self.fecha_vacunacion=fecha_vacunacion
        else:
            pass

    def obtener_perro(self):
        self.miperro

    def obtener_bovino(self):
        self.mibovino
        
