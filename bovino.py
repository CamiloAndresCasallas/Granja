from animal import animal


class Bovino(animal):
    def __init__(self) :
        self.propietario=""
        self.Fecha_vacunacion=""
        self.establo=""

    def pastar(self):
        if self.establo<=5:
            print ("pastar")
        elif self.establo >5:
            print("no pastar")

    def emitir_sonido(self):
        print ("Muuu")


