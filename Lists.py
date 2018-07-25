lista = [1, "dos", False, [45, "cien"], (9,8,7), "g"]

for x in range(0,len(lista)):
    print(lista[x])

print(lista[3][0])
print(lista[4][0])

lista[-1] = "h"
print(lista)

otraLista = [1,2,3,4,5,6,7,8,9,10]
print(otraLista[0:5])
print(otraLista[5:10])
print(otraLista[4:])
print(otraLista[:6])
print(otraLista[0:10:2])
nuevaLista = [11, 12, 13, 14, 15]
otraLista.extend(nuevaLista)
print(otraLista)

frase = "Esto es una frase".split()
print(frase)

chatDirections = set(["inbound", "outbound", "inbound", "outbound"])
print(chatDirections)