# zad3

f = open("zadanie.txt")
b = f.read()

a = b.lower()
dict = {}
for x in a:
    if x.isalpha():
        if x not in dict.keys():
            dict.update({x: 1})
        else:
            dict[x] += 1
print(dict)

f.close()
