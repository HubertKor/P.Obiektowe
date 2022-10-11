#zad 2.1
def mult(a):
    wynik = 1
    for x in range(0,len(a)):
        wynik*=a[x]
    return wynik
print(mult(range(1,8,2)))

#zad 2.2
def mult_ins(a):
    wynik = 1
    for x in range(0,len(a)):
        if type(a[x]) == int:
            wynik*=a[x]
    return wynik
print(mult_ins([3,3.14,5,"abc",7]))

#zad 2.3
def multiply(*args):
    wynik = 1
    for x in args:
        wynik*=x
    return wynik
print(multiply(3,5,7))

#zad 2.4
def multiply_ints(*args):
    wynik = 1
    for x in args:
        if type(x) == int:
            wynik *= x
    return wynik
print((multiply_ints(3,5,7)))

#zad 2.5
def make_car(firma,model,**kwargs):
    slownik = kwargs
    slownik["firma"]=firma
    slownik["model"]=model
    return slownik
print(make_car("Kia","Picanto", kolor = "cafe mocca" ,poj_silnika = 900, ))

#zad 3.1
def zad31():
    lista = []
    lista.append([x for x in range(1,11)])
    lista.append([x ** 2 for x in range(1,11)])
    lista.append(([x ** 3 for x in range(1,11)]))
    for x in lista:
        for y in x:
            print(y)
print(zad31())

#zad 3.2
def zad32():
    lista = []
    aktualnaliczba = 1
    dlugoslisty = 1
    for i in range(0,10):
        lista.append([])
        for j in range(dlugoslisty):
            lista[i].append(aktualnaliczba)
            aktualnaliczba+=1
        dlugoslisty+=1


    suma=0
    iterator=0
    for i in lista:
        arraySum = 0
        for j in i:
            arraySum += j
        suma += arraySum
        print(f'Array[{iterator}] sum == {arraySum}')
        iterator += 1
    print(f'Total sum == {suma}')

print(zad32())

#zad 3.2.1

def sum(a,b):
    n = 3
    c = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = a[i][j] + b[i][j]
    return c
    print(c)
print(sum([[3,2,1],[-1,2,3],[1,2,3]],[[3,2,1],[-1,2,3],[1,2,3]]))

#zad 3.2.2

def product(a,b):
    n = 3
    c = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] = c[i][j] + a[i][k] * b[k][j]
    return c
    print(c)


print(product([[3, 2, 1], [-1, 2, 3], [1, 2, 3]], [[3, 2, 1], [-1, 2, 3], [1, 2, 3]]))

#zad 3.2.3

def mult1(a,x):
    n = 3
    c = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = a[i][j] * x
    return c
print(mult1([[3,2,1],[-1,2,3],[1,2,3]],3))

#zad 3.2.4

def transp(a):
    n=3
    a_tr = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            a_tr[j][i] = a[i][j]
    return a_tr
print(transp([[2,3,1],[2,3,4],[4,2,3]]))