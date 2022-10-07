# def division(a, b):
#     return a / b
#
#
# def calcular():
#     division(1, 0)
#
#
# try:
#     calcular()
# except:
#     print("No se puede dividir por cero hombreeee")
####################################################
try:
    num = int("3a")
    print("no_existe")
except NameError:
    print("La variable no existe")

except ValueError:
    print("El valor no es un numero")

###############################################3

try:
    num = int("3a")
    print("no_existe")
except (NameError, ValueError):
    print("Ocurrio un error")

###############################################

try:
    num = 33
except:
    print("Hubo un error!!")
else:
    print("Todo esta bien!!")

###############################################

try:
    y = 0
    x = 4
    z = x / y
except ZeroDivisionError:
    print("Division por cero00")
finally:
    print("Limpiando")


#############Pildoras Informaticas############

def evaluaEdad(edad):
    if edad < 0:
        # especificar el tipo de excepcion cuando se cumpla esa excepcion
        raise TypeError("No se permiten edades negativas")  # se puede cambiar la naturaleza de la excepcion
    if edad < 20:
        return "Eres muy joven"
    elif edad < 40:
        return "Eres joven"
    elif edad < 65:
        return "Eres maduro"
    elif edad < 100:
        return "Cuidate..."


print(evaluaEdad(-12))
