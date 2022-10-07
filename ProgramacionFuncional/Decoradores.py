# podríamos querer añadir la funcionalidad de que se imprimiera el
# nombre de la función llamada por motivos de depuración:
import cmath


def mi_decorador(funcion):  # Funcion A recibe por parametro una funcion B
    def nueva(*args):  # funcion C, que nos devolveria el decorador con un return
        print("Llamada a al funcion", funcion.__name__)
        retorno = funcion(*args)
        return retorno

    return nueva


@mi_decorador
def pi():
    return cmath.pi


print(pi())
