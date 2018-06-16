lista = [1, "dos", False, [45, "cien"], (9,8,7), "g"]

for x in range(0,len(lista)):
    print(lista[x])

print(lista[3][0])
print(lista[4][0])

lista[-1] = "h"
print(lista)