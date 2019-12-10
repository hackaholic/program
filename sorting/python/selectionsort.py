""" The selection sort algorithm sorts an array by repeatedly finding the minimum element 
            (considering ascending order) from unsorted part and putting it at the beginning.
"""

import sys

data = list(map(int, open(sys.argv[1]).read().strip("\n").split("\n")))

for x in range(len(data)):
    min_index = x;
    for y in range(x+1, len(data)):
        if data[min_index] > data[y]:
            min_index = y;
    if min_index != x:
        data[x], data[min_index] = data[min_index], data[x]

print(data)
