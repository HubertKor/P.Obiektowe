# zad6

def przemienna(list):
    sum = 0
    znak = 1
    for x in list:
        sum += x * znak
        znak *= -1
    return sum


lista = [1, 4, 16, 9, 9, 7, 4, 9, 11]
print(przemienna(lista))
