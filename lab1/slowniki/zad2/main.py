#zad2

dict = {}
while True:
    a = input()
    if not a:
        break
    else:
        if a not in dict:
            dict.update({a: 1})
        else:
            dict[a] += 1
print(dict)
