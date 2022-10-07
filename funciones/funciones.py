# def mi_funcion(param1, param2):
#     print(param1)
#     print(param2)

# mi_funcion("hola", 4)
# mi_funcion(param2="hola", param1=4)#se puede cambiar el orden

# veces que se repite un parametro
# def printVeces(texto, veces):
#     print(texto * veces)

# printVeces("hi ", 3)

######### número variable de argumentos#######
# def varios(arg1, arg2, *otros):
#     for val in otros:
#         print(str(val))#cast int a string str()

# otros=(1, 4, "hi", 54, 23, "hola", "mundoki")
# # varios(1, 2) # resultado vacio
# # varios(1, 5, 8)# resultado solo 8
# varios(1, 2, 5, otros) # resultado salen desde el 5 en adelante

######### preceder el ultimo parametro#######
# def variosPre(arg1, arg2, **otros):
#     for i in otros.items():#funcion items() de diccionarios
#         print(i)

# variosPre(1, 2, tercero=3)

# Demostracion de paso por valor de referencia a objetos########3
###ver teoria.md###
# def f(x, y, z):
#     x = x+3
#     y.append(23)
#     z=z+4
#     print(x, y, z)

# x = 22 #int inmutable
# y = [22] #lista mutable
# z=(22) #tupla inmutable
# f(x, y, z)
# print(x, y, z)

# Como vemos la variable x no conserva los cambios
# una vez salimos de la función porque los enteros 
# son inmutables en Python.  Sin embargo la variable 
# y si los conserva, porque las listas son mutables.
# En resumen: los valores mutables se comportan como 
# paso por referencia, y los inmutables como paso por valor.

######devolver valores con return#######
# def sumar (x, y):
#     return (x + y)
# print(sumar(3, 5))


######varios valores que retorna a return##########
def f(x, y):    
    return x * 2, y * 2
a, b = f(3, 5)
# Sin embargo esto no quiere decir que las funciones
# Python puedan devolver varios valores, en realidad
# crea una tupla al vuelo y la retorna
# print(type((a, b)))
# print(a, b)# tupla demostracion L de arriba
print(a)
print(b)