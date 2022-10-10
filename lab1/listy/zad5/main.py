# zad5
def minmax(list):
    mini = list[0]
    maks = list[0]
    for i in range(1, len(list)):
        if list[i] < mini:
            mini = list[i]
        if list[i] > maks:
            maks = list[i]
    tup = (mini, maks)
    return tup


lista = [2322, 5, 32, 12, -31, 23, -2, -231, 222]
print(minmax(lista))
