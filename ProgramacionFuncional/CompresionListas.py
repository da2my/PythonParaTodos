l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Esta expresión se leería como “para cada n en l haz n ** 2”.
l2 = [n ** 2 for n in l]
print(l2)

l2 = [n for n in l if n % 2.0 == 0]
print(l2)

l = [0, 1, 2, 3]
m = ["a", "b"]
n = [s * v for s in m
     for v in l
     if v > 0]
print(l)
# for-in anidados equivale a la contruccion de arriba
l = [0, 1, 2, 3]
m = ["a", "b"]
n = []
for s in m:
    for v in l:
        if v > 0:
            n.append(s * v)
print(l)
