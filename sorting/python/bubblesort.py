"""Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the 
           adjacent elements if they are in wrong order.
"""

import sys
import time
data = list(map(int, open(sys.argv[1]).read().strip().split("\n")))

def method1():
    i = 0
    n = len(data)
    flag = False
    while True:
        if i<n and data[i] > data[i+1]:
            data[i], data[i+1] = data[i+1], data[i]
            flag = True
        i += 1
        if i+1 == n:
            i = 0
            if not flag:
                break
            flag = False
    print(data)

method1()
