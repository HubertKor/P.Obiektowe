# zad9
# a

def foo(list):
    list[0], list[len(list) - 1] = list[len(list) - 1], list[0]


lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
foo(lista)
print(lista)
# b

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def foo1(list):
    temp = list[-1]
    list.pop(-1)
    list.insert(0, temp)


foo1(lista)
print(lista)


# c
def foo2(list):
    for x in list:
        if x % 2 == 0:
            list[x] = 0


lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
foo2(lista)
print(lista)


# d

def foo3(list):
    a = list.copy()
    for i in range(1, len(list) - 1):
        if a[i - 1] > a[i + 1]:
            list[i] = a[i - 1]
        else:
            list[i] = a[i + 1]


lista = [0, 4, 2, 3, 5, 9]
foo3(lista)
print(lista)


# e

def foo4(list):
    if len(list) % 2 == 1:
        del list[len(list) // 2]
    else:
        del list[int(len(list) / 2)]
        del list[len(list) // 2]


lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
foo4(lista)
print(lista)


# f

def foo5(list):
    j = 0
    for i in range(len(list)):
        if list[i] % 2 == 0:
            temp = list[i]
            list.pop(i)
            lista.insert(j, temp)
            j += 1


lista = [0, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]
foo5(lista)
print(lista)


# g

def foo6(list):
    list.sort()
    return list[-2]


lista = [0, 1, 5, 4, 2, 3, 8, 7, 9, 6]
print(foo6(lista))


# h
def foo7(list):
    for i in range(1, len(list) - 1):
        if list[i] < list[i - 1] or list[i] > list[i + 1]:
            return False
    return True


lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 8]
print(foo7(lista))


# i
def foo8(list):
    for i in range(len(list) - 1):
        if list[i] == list[i + 1]:
            return True
    return False


lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(foo8(lista))


# j
def foo9(list):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] == list[j]:
                return True
    return False


lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(foo9(lista))
