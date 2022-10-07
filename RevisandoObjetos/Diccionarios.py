from ast import For


D = {"Love Actually": "Richard Curtis",
     "Kill Bill": "Tarantino",
     "Amélie": "Jean-Pierre Jeunet"}

l = ["una lista", [1, 2]]

print(D)  # muestra todo el objeto

# si no encuentra la clave devuelve un null o none
valor = D.get("Love Actually")
# si no encuentra la clave lanza una excepcion
# valor = D.get("Love Actually   ")
print(valor)

# deprecated -> D.has_key('Love Actually')
# print(D.has_key("Love Actually"))
contieneEstaKey = "Love Actually" in D
print(contieneEstaKey)

# lista de tuplas con pares clave-valor
lista = D.items()
print(lista)

# lista de las claves del diccionario.
listaKeys = D.keys()
print(listaKeys)

# Borra la clave k del diccionario y devuelve su valor. Si no se encuentra
# dicha clave se devuelve d si se especificó el parámetro o bien se lanza
# una excepción
valor = D.pop("Love Actually")
print(valor)

# Devuelve una lista de los valores del diccionario
D.values()
print(D)

print()
# D.count(l[, start[, end]])

str = "this is string example....wow!!!";

sub = "i";
print ("str.count(sub, 4, 40) : ", str.count(sub, 0, len(str)))

for i in range(5):
     valor[i:i + len(sub)] == sub
     print(valor)


