# La lista en Python son variables que almacenan arrays,
# internamente cada posición puede ser un tipo de datos
# distinto.

# l=["una lista", [1, 2]]
# l = [11, False]#se sobreescriben

# mi_var = l[3] # muestra cada posicion de la lista
# mi_var=l[1][1]# Al tener dos elementos en la lista. En el primer parametro [se pone de q elemento cojes] y el otro [de que indice cojes]
# print (mi_var)

##################

l = [98, "Laura", True, "Una lista", [1, 2]]  # (inicio:fin)

#mi_var = l[4][1]

# slicing o particionado:
# mi_var= l[1:4]# (inicio:fin) como un substring, sin incluir el ultimo
# print(mi_var)
# mi_var=l[1:4:2]#(inicio:fin:salto) ##no entiendo el salto ##determi-nar cada cuantas posiciones añadir un elemento a la lista.

# no es necesario indicar el principio y el final del slicing,
# sino que, si estos se omiten, se usarán por defecto las posiciones de inicio y fin de la lista
# mi_var = l[1:]
# mi_var = l[::3] # el numero hace referencia que elemento de la lista accedo
# l[0:2] = [5, 3]
# l[0:2] = [False]
# mi_var = l

# uso de numeros negativos para acceder a las
# posiciones de la lista, en este caso -1
# se dirige a la ultima posicion, -2 al pelultimo:
# mi_var=l[-1]

print(mi_var)
