# zad 1
A = [1+x for x in range(0, 10)]
print(A)
B = [2*x for x in range(0, 11)]
print(B)
C = [x**2 for x in range(1,11)]
print(C)
D = [x*0 for x in range(1,10)]
print(D)
E = [x%2 for x in range(0,10)]
print(E)
f = [x%5 for x in range(0,10)]
print(f)
# zad 2
listaA = []
A = 1
while A in range (0,11):
     listaA.append(A)
     A+=1
print(listaA)

listaB = []
B = 0
while B in range (0,21):
     listaB.append(B)
     B+=2
print(listaB)
listaC = []
C = 1
while C in range (0,11):
     listaC.append(C**2)
     C+=1
print(listaC)

listaD = []
C = 1
while C in range (0,11):
     listaD.append(C*0)
     C+=1
print(listaD)

listaE = []
C = 0
while C in range (0,10):
     listaE.append(C%2)
     C+=1
print(listaE)

ListaF= []
F=0
while F in range(0,10):
     ListaF.append(F%5)
     F+=1
print(ListaF)

#zad 3
def ile_ujemnych(lista):
     licznik = 0
     for x in lista:
         if(x<0):
             licznik+=1
     print(licznik)
lista1 = [-1, -2, -8, -1, -5, 6, 7, -3]
ile_ujemnych((lista1))
#zad 4
def iloczyn(lista):
     wynik = 1
     for x in lista:
          wynik = wynik * x
     print(wynik)
list = [2,12,1,5,1]
iloczyn(list)
#zad 5
def minmax(lista):
     return (min(lista), max(lista))
lista =[31, 28, 31, 30, 31, 30, 31, 31,30, 31, 30, 31]
print(minmax(lista))
#zad 6
def suma(lista):
     wynik = 1
     suma = 0
     for x in lista:
          suma += wynik*x
          wynik = -wynik
     print(suma)
listaa = [1, 4, 16, 9, 9, 7, 4, 9, 11]
suma(listaa)
# # zad 7
i = 0
listaBAA = []
while i < 10:
     x = input()
     while x in listaBAA:
          print("juz jest na liscie")
          x = input()
     listaBAA.append(x)
     i += 1
print(listaBAA)

