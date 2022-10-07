from functools import reduce


# map(function, sequence[, sequence, ...])
# La función map aplica una función a cada elemento de una secuencia y
# devuelve una lista con el resultado de aplicar la función a cada elemen-
# to. Si se pasan como parámetros n secuencias, la función tendrá que
# aceptar n argumentos. Si alguna de las secuencias es más pequeña que
# las demás, el valor que le llega a la función function para posiciones
# mayores que el tamaño de dicha secuencia será None.


def cuadrado(n):
    return n ** 2


l = [1, 2, 3, 4, 5]
l2 = map(cuadrado, l)


# for i in l2:
#     print(i)


# filter(function, sequence)
# La funcion filter verifica que los elementos de una secuencia cum-
# plan una determinada condición, devolviendo una secuencia con los
# elementos que cumplen esa condición. Es decir, para cada elemento de
# sequence se aplica la función function ; si el resultado es True se añade
# a la lista y en caso contrario se descarta.

def es_par(n):
    return n % 2.0 == 0


l = [1, 2, 3, 4, 5, 6]
l2 = filter(es_par, l)


# for i in l2:
#     print(i)


# reduce(function, sequence[, initial])
# La función reduce aplica una función a pares de elementos de una
# secuencia hasta dejarla en un solo valor.
# A continuación podemos ver un ejemplo en el que se utiliza reduce
# para sumar todos los elementos de una lista.
def sumar(x, y):
    return x + y


l = [1, 2, 3, 4, 9] #calcula((((1+2)2+3)6+4)10+9) = 19
l2 = reduce(sumar, l)
print(l2)
