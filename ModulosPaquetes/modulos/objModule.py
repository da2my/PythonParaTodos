# en Python los módulos también son objetos; de tipo module en concreto.
# Por supuesto esto significa que pueden tener atributos y métodos.
# Uno de sus atributos, __name__ , se utiliza a menudo para incluir código
# ejecutable en un módulo pero que este sólo se ejecute si se llama al módulo
# como programa, y no al importarlo. Para lograr esto basta saber que cuando
# se ejecuta el módulo directamente __name__ tiene como valor “__main__”, mientras
# que cuando se importa, el valor de __name__ es el nombre del
# módulo:

print("Se muestra siempre")
if __name__ == "__main__":
    print("Se muestra si no es importacion")

print(__doc__)  # como utilizao aqui esta funcion __doc__
