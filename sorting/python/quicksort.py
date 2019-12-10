"""QuickSort is a Divide and Conquer algorithm. It picks an element as pivot 
and partitions the given array around the picked pivot. """

import sys

data = list(map(int, open(sys.argv[1]).read().strip("\n").split("\n")))
print(data)

def partition(a, start, end):
    pivot = a[end]
    pivot_index = start
    for i in range(start, end):
        if(a[i] < pivot):
            a[i], a[pivot_index] = a[pivot_index], a[i]
            pivot_index +=1

    a[end], a[pivot_index] = a[pivot_index], a[end]
    return pivot_index

def quicksort(a, start, end):

    if(start < end):
        pivot_index = partition(a, start, end)
        quicksort(a, start, pivot_index-1)
        quicksort(a, pivot_index+1, end)

quicksort(data, 0, len(data)-1)
print(data)
