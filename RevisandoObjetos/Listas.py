class UnaClase(object):  # En el nuevo estilo las clases heredan de object.
    def __init__(self):
        print('I am a jazzy new class')


unObj = UnaClase()
otroObj = UnaClase

L = [8, 4, 8, "una lista", [1, 2]]
L.append(unObj)
print(" - ", L)

num = L.count(8)
print(" - Hay ", num, " numeros de 8 en la lista")

anexarLista = [2, 4, 6, 8, 10]
L.extend(anexarLista)
print(" - Despues de anexar otra lista: ", L)

print(" - este valos esta en la posicion: ", L.index(unObj))

L.insert(2, otroObj)
print(" - asi queda la lista:", L)

pos = L.pop(0)  # si no se especifica posicion se coje la ultima de la lista
print(" - asi queda la lista despues de eliminar el elemento", pos, ":", L)

L.remove(unObj)  # elimina el primer elemento que pasamos por parametro
print(" - asi queda la lista:", L)

L.reverse()
print(" - asi queda la lista:", L)

list = [9, 6, 10, 1, 8, 5, 3, 7, 4, 2]
list.sort()  # aprender a usar L.sort(cmp=None, key=None, reverse=False)
print(" - ", list)
