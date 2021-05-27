
import time
import math


def swap(array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp


# find partition position
def partition(array, first, last):
    # setting pivot as median of three element
    pivot = median_of_three(array, first, last)
    # indexing of smaller element
    i = first - 1
    # traverse all elements compare each of elements with pivot
    for j in range(first, last):
        if array[j] <= pivot:
            i += 1
            swap(array, i, j)
    # swaping the pivot with the greater element
    swap(array, i + 1, last)
    return i + 1


def quick_sort(array, first, last):
    if first < last:
        # p is pivot index after partitioning
        p = partition(array, first, last)
        # recursively sort, left and right of pivot
        quick_sort(array, first, p - 1)
        quick_sort(array, p + 1, last)


def median_of_three(array, left, right):
    mid = math.ceil((left + right) / 2)
    if array[left] > array[mid]:
        swap(array, left, mid)
    if array[left] > array[right]:
        swap(array, left, right)
    if array[mid] > array[right]:
        swap(array, mid, right)
    swap(array, mid, right)
    return array[right]


arr = [5, 4, 2, 7, 9, 1, 6, 10, 8]
n = len(arr)
print("Given array is")
for i in range(n):
    print("%d" % arr[i]),

quick_sort(arr, 0, n - 1)
print("\n\nSorted array is")
for i in range(n):
    print("%d" % arr[i])
    

with open("reversed_100.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)

    word = [int(i) for i in word]
    t_start = time.time()
    quick_sort(word, 0, len(word)-1)
    t_end = time.time()
    print("Sorted array is:")
    for i in range(len(word)):
        print(word[i], end=" ")
    print("")
    print(f"Time complexity for quickSort_MOT {t_end-t_start}")
