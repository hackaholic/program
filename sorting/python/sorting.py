
import sys

class Sorting:
    def __init__(self, file):
        """ Input is read from a file, where each line contains an element"""
        self.data = [ int(x) for x in open(file).read().strip().split("\n")]
        self.length = len(self.data)

    def selection_sort(self):
        """ The selection sort algorithm sorts an array by repeatedly finding the minimum element 
            (considering ascending order) from unsorted part and putting it at the beginning.
        """
        for i in range(self.length):
            min_index = i
            for j in range(i+1, self.length):
                if self.data[min_index] > self.data[j]:
                     min_index = j
            if min_index != i:
                self.data[i], self.data[min_index] = self.data[min_index], self.data[i]

    def bubble_sort(self):
        """Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the 
           adjacent elements if they are in wrong order.
        """
        for i in range(self.length):
            flag = False
            for j in range(self.length-i-1):
                if self.data[j] > self.data[j+1]:
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]
                    flag = True
            if not flag:
                break

    def display(self):
        print(self.data)

if __name__ == "__main__":
    s = Sorting('sample.txt')
    s.bubble_sort()
    s.display()
