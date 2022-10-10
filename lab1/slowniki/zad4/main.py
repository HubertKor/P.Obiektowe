#zad4

f = open("zadanie.txt")
lines = f.readlines()

dict = {}
for l in lines:
    a = l.split()
    for x in a:
        if x.isnumeric():
            if x not in dict:
                dict.update({x: 1})
            else:
                dict[x] += 1
print(dict)

f.close()
