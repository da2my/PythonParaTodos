class MiError(Exception):
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return "Error " + str(self.valor)


try:
    resultado = 0
    if resultado > 20:
        raise MiError(33)
except (MiError, TypeError):
    print(TypeError)
