# HERENCIA

class Instrumento:
    def __init__(self, precio):
        self.precio = precio

    def tocar(self):
        print("Estamos tocando musica")

    def romper(self):
        print("Eso lo pagas tu")
        print("Son", self.precio, "$")

class Bateria(Instrumento):
    def __init__(self, miInstrumento):
        self.miInstrumento= miInstrumento

    def tocarBateria(self):
        print("Tocando la bateria con", self.miInstrumento)
    pass

class Guitarra(Instrumento):
    pass


mi_instumento = Instrumento(20.56)
mi_instumento.tocar()
mi_instumento.romper()


mi_instumento= Bateria("baquetas")
mi_instumento.tocarBateria()
mi_instumento.tocar()

mi_instumento= Bateria("platillos")
mi_instumento.tocarBateria()
mi_instumento.tocar()