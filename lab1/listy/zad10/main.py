#zad10
def equals(a,b):
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True
list1 = [1,2,3,"a",5]
list2 = [1,2,3,"A",5]
print(equals(list1,list2))