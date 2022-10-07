# El operador lambda sirve para crear funciones anónimas en línea. Al ser
# funciones anónimas, es decir, sin nombre, estas no podrán ser referen-
# ciadas más tarde.
# Las funciones lambda se construyen mediante el operador lambda , los
# parámetros de la función separados por comas (atención, SIN parénte-
# sis), dos puntos ( : ) y el código de la función.

# Las funciones lambda están restringidas por la sintaxis a una sola expresion
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

l2 = filter(lambda n: n % 2.0 == 0, l)

for i in l2:
    print(i)


## LA FUNCION LAMBDA SUSTITUYE A:

# def es_par(n):
#     return n % 2.0 == 0


# l = [1, 2, 3, 4, 5, 6]
# l2 = filter(es_par, l)