#zad1
#a
lista = [x for x in range(1,11)]
print(lista)
#b
lista = [x for x in range(0,21,2)]
print(lista)
#c
lista = [x**2 for x in range(1,11)]
print(lista)
#d
lista = [0 for x in range(10)]
print(lista)
#e
lista = [0 if x%2==1 else 1 for x in range(1,11)]
print(lista)
#f
lista = []
for i in range(2):
    for j in range(5):
        lista.append(j)
print(lista)
