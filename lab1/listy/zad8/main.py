# zad8
lista = []
for x in range(2, 10001):
    lista.append(x)

for x in lista:
    if (x % 2 == 0 and x != 2):
        lista.remove(x)

for x in lista:
    if (x % 3 == 0 and x != 3):
        lista.remove(x)

print(lista)

