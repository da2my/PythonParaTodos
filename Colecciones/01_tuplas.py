t = (1, 2, True, "python")

t= 1, 2, 3

#t=(1)
mi_var = t[0] 
mi_var = t[1:3]
#print(mi_var)

c="hola mundo"
tpl=c[0]   # h
tpl=c[5:]  #mundo 
tpl=c[::3] # hauo -> h 0,1,2 a 0,1,2 u 0,1,2 o  

print(tpl)

# las tuplas al ser inmutables no las podemos modificar
# (no se pueden añadir ni eliminar elementos a una tupla)
# nos da error -> TypeError
# t[2]=False
print(t)

