""" Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.

Shift the element until its get ot its right position"""


import sys

data = list(map(int, open(sys.argv[1]).read().strip("\n").split("\n")))

print(data)

for i in range(len(data)-1):
    if data[i] > data[i+1]:
        data[i], data[i+1] = data[i+1], data[i]
        k = i
        while k>0  and data[k-1] > data[k]:
            data[k-1], data[k] = data[k], data[k-1]
            k -= 1

print(data)
