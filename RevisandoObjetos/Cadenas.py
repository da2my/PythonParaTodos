S = "un cadena de texto de la patrulla canina"
sub = "a"
veces = S.count(sub, 30, 50)
print(" - Veces que se repite el caracter sub: ", veces)

vezPrimera = S.find(sub)
print(" - Se encuentra por primera vez en la cadena en la posicion: ", vezPrimera)

s = " "
seq = (" - Laila,", "hora", "de", "dormir")
cadena = s.join(seq)
print(cadena)

cadena = S.partition("texto")  # devuelve tupla
print(" - ", cadena)

cadena = S.replace("un", "una")
# cadena = S.replace("un", "una", 0)
print(cadena)

cadena = S.split()  # devuleve una lista de las palabras separadas con espacio
print(" - ", cadena)

cad = "es:un:separador:con:split:y:dos:puntos"
cadena = cad.split(":")  # para que funciones cad.split(":") que es el separador
print(" - ", cadena)


