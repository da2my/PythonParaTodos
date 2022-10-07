# si el nombre comienza con dos guiones bajos => variable o funcion "private"
# si el metodo comienza y termina con dos guiones bajos son metodos especiales (ver detalles en teoria)

class Ejemplo:
    def publico(self):
        print("Publico")

    def __privado(self):
        print("Privado")


# ej = Ejemplo()
# ej.publico()

# ej.__privado()##LANZA EXCEPCION POR QUERER ACCEDER A UN METODO PRIVADO
# ej.privado()##LANZA EXCEPCION POR QUERER ACCEDER A UN METODO PRIVADO

# Este mecanismo se basa en que los nombres que comienzan con un
# doble guión bajo se renombran para incluir el nombre de la clase
# (característica que se conoce con el nombre de name mangling). Esto
# implica que el método o atributo no es realmente privado, y podemos
# acceder a él mediante una pequeña trampa:
# ej._Ejemplo__privado()  ###TRAMPA PARA ACCEDER A UN METODO PRIVADO


# En ocasiones también puede suceder que queramos permitir el acceso
# a algún atributo de nuestro objeto, pero que este se produzca de forma
# controlada. Para esto podemos escribir métodos cuyo único cometido
# sea este, métodos que normalmente, por convención, tienen nombres
# como getVariable y setVariable ; de ahí que se conozcan también con
# el nombre de getters y setters.
class Fecha():#poner entre el parentesis object, es usar nuevo-estilo
    def __init__(self):  # constructor
        self.__dia = 1

    def getDia(self):
        return self.__dia

    def setDia(self, dia):
        if dia > 0 and dia < 33:  # 0 < dia < 33
            self.__dia = dia
        else:
            print("Error")

    dia = property(getDia, setDia)  # ??si quito esta linea funciona igual??


mi_fecha = Fecha()
mi_fecha.setDia(27)
print(mi_fecha.getDia())



