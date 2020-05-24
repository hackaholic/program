import sys

data = list(map(int, open(sys.argv[1]).read().strip("\n").split("\n")))
print(data)

def mergeSort(arr):

    if len(arr) > 1:
        mid = len(arr)//2
        arrL, arrR = arr[:mid], arr[mid:]
        mergeSort(arrL)
        mergeSort(arrR)
        i, j, k = 0, 0, 0
        while i<len(arrL) and j<len(arrR):
            if arrL[i] > arrR[j]:
                arr[k] = arrR[j]
                j += 1
            else: 
                arr[k] = arrL[i]
                i += 1
            k +=1
        while i < len(arrL):
            arr[k] = arrL[i]
            k += 1
            i += 1

        while j < len(arrR):
            arr[k] = arrR[j]
            k += 1
            j +=1

mergeSort( data)
print(data)
