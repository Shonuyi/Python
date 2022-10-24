
from random import randrange

N = 10
a1 = [randrange(500) for n in range(N)]
a2 = [randrange(500) for n in range(N)]

def combine(a1, a2):
    a3 = list()
    for i in a1:
        for j in a2:
            if j != i and j not in a3:
                a3.append(j)
        if i != j and i not in a3:
            a3.append(i)

    return a3

def sort(array):
    for i in range(len(array)-1):
        mini = array[i]
        for j in range(i, len(array)):
            if array[j] < mini:
                mini = array[j]
        array[array.index(mini)], array[i] = array[i], mini

    return array

a3 = combine(a1, a2)
print("Test program with an N value of 10")
print()
print(a1)
print(a2)
print(sort(a3))
