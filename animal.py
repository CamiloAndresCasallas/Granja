class animal:
    def __init__(self):
        self.peso=""
        self.edad=""
        self.raza=""

    def correr(self):
        if self.edad >=5:
            print("rapido")
        else:
            print("lento")



    def emitirsonido(self):
        pass



    def obteneredad(self):
        return self.edad