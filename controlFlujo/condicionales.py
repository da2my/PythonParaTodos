fav = "mundogeek.net"
# si (if) fav es igual a "mundogeek.net"
if fav == "mundogeek.net":
    print("Tienes buen gusto!")
else:
    print("No Gracias")

print("**********************\n**********************")

numero = -54
if numero < 0:
    print("Negativo")
elif numero > 0:
    print("Positivo")
else:
    print("Cero")

############if termario###########
print("""**********
Numero par o impar:
""")
num=3474
print("El numeros: ", num)
var = "par" if (num % 2 == 0) else "impar" # Ternario diferente q en Java
print(var)

edad = input("¿Que edad tienes?")
var = "mayor" if (int(edad) > 18) else "menor" 
print("Eres ", var, " de edad!")