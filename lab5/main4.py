#zad 1

import array

print(dir(array))

#zad2

class zad2():
    def zad(self):
        return

print(dir(zad2()))

#zad3

class zad3():
    def __init__(self):
        self.name = 'zad3'

d = zad3()
print(dir(d))

#zad4

print(dir(abs(1)))
liczba = -155
print(abs(liczba))

#zad5

class Student(object):
    def __init__(self, nazwa_ucznia: str, klasa_ucznia: str, student_id: int) :
        self.nazwa_ucznia = nazwa_ucznia
        self.klasa_ucznia = klasa_ucznia
        self.student_id = student_id

Dziennik = Student("Robercik", "3a", 0)
print(Dziennik.nazwa_ucznia)
print(Dziennik.klasa_ucznia)
print(Dziennik.student_id)

#zad6
class Student1(object):
    def __init__(self, nazwa_ucznia: str, klasa_ucznia: str, student_id: int) :
        self.nazwa_ucznia = nazwa_ucznia
        self.klasa_ucznia = klasa_ucznia
        self.student_id = student_id

    def student_data(self):
        print(self.student_id)
        if self.nazwa_ucznia or self.klasa_ucznia is not None:
            print(self.nazwa_ucznia, self.klasa_ucznia)

Dzien = Student1("adas","3a",1)
print(Dzien.student_data())


#zad7
class Student2:
    def __init__(self):
        self.name = "Zad7"

b = Student2()
print(type(b))
print(dir(b.__dict__))
print(dir(b.__module__))


#Zad8
class Student3:
    def __init__(self):
        pass

class Marks:
    def __init__(self):
        pass

s = Student3()
m = Marks()

print(isinstance(m,Marks))
print(isinstance(s,Student3))

print(issubclass(Student3,object))
print(issubclass(Marks,object))

#Zad9

class Student4():
    def __init__(self):
        self.student_name = "Krzychu"
        self.marks =  [4,5,6]



o = Student4()
print(o.student_name)
print(o.marks)

o.student_name = "zbychu"
o.marks = [4,3,2]
print(o.student_name)
print(o.marks)



