#zad2
#a
lista = []
i = 1
while i < 11:
    lista.append(i)
    i += 1
print(lista)
#b
lista = []
i = 0
while i < 21:
    lista.append(i)
    i += 2
print(lista)
#c
lista = []
i = 1
while i < 11:
    lista.append(i**2)
    i += 1
print(lista)
#d
lista = []
i = 0
while i < 10:
    lista.append(0)
    i += 1
print(lista)
#e
lista = []
i = 0
while i < 10:
    if i%2==0:
        lista.append(0)
    else:
        lista.append(1)
    i += 1
print(lista)
#f
lista = []
i = 0
while i < 2:
    j = 0
    while j < 5:
        lista.append(j)
        j += 1
    i += 1
print(lista)
