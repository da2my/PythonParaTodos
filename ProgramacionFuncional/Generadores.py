l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

l2 = (n ** 2 for n in l)

print(l2)


# Veamos por ejemplo un generador que devuelva
# números de n a m con un salto s .
def mi_generador(n, m, s):
    while n <= m:
        yield n
        n += s


# x = mi_generador(0, 10, 1)
# print(x)  # no pinta

for n in mi_generador(0, 5, 2):  # de 0 a 5 con saltos de 2
    print(n)  # pinta

# lista = list(mi_generador) # excepcion!!!!!!!!!!

# for n in lista:
#     print(n)
