## Clases y objetos

class Coche:
    """Abstraccion de los objetos coche."""

    def __init__(self, gasolina):#inicia y termina con 2 guiones bajos es un metodo especial
        self.gasolina = gasolina
        print("Tenemos", gasolina, "litros")

    def arrancar(self):
        if self.gasolina > 0:
            print("Arranca")
        else:
            print("No arranca")

    def conducir(self):
        if self.gasolina > 0:
            self.gasolina -= 1
            print("Quedan", self.gasolina, "litros")
        else:
            print("No se mueve")




mi_cocher = Coche(3)
mi_cocher.arrancar() 
mi_cocher.conducir()
mi_cocher.conducir()
mi_cocher.conducir()
# mi_cocher.conducir()
mi_cocher.arrancar() 

