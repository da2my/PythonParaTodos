# En el ejemplo de Encapsulacion os habrá llamado la atención el hecho de que la
# clase Fecha derive de object
class OldClass:  # En el estilo antiguo, las clases no heredan de nada.
    def __init__(self):
        print('I am an old class')


class NewClass(object):  # En el nuevo estilo las clases heredan de object.
    def __init__(self):
        print('I am a jazzy new class')


old = OldClass()
# Salida: I am an old class

new = NewClass()
# Salida: I am a jazzy new class
