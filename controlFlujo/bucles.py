
# edad = 0
# while edad < 18:
#     edad = edad + 1
#     print ("Felicidades, tienes", str(edad))

#WHILE#####Sale condicion de bucle con break################
# while True:
#     entrada = input("> ")
#     if entrada == "adios":
#         break
#     else:
#         print(entrada)

#WHILE#####Sale condicion de bucle con boolean################

# salir = False
# while not salir:
#     entrada = input("> ")
#     if entrada == "adios":
#         salir = True
#     else:
#         print(entrada)

#WHILE######Saca solo inpares porque if es para pares, hasta legar a 18 por el while##############
# edad = 0
# while edad < 18:
#     edad = edad + 1
#     if edad % 2 == 0:
#         continue
#     print("Felicidades, tienes " + str(edad))

#for ... in########foreach de java###########
# secuencia = ["uno", "dos", "tres"]#lista
# for elemento in secuencia:
#     print (elemento)

#for ... in########con funcion range()##########
for a in range(50, 75, 3):  # --> prints 1 through 99 number
    print(a, end=", ") # end=""

