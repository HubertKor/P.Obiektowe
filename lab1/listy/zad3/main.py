#zad3
def ile_ujemnych(list):
    i=0
    for x in list:
        if x < 0:
            i += 1
    return i
lista = [1,2,-3,4,5]
print(ile_ujemnych(lista))
