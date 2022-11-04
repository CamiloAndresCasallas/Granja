from animal import animal

class Perro(animal):

    def __init__(self):
        self.propietario=""
        self.Fecha_vacunacion=""

    def emitirsonido(self):

        if self.edad >=3:
            print("gua gua")
        elif self.edad <3:
            print("auf auf")


    