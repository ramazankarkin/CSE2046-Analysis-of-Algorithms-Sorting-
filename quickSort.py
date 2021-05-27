import time
# pass index of array to swap
def swap(array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp


def partition(array, first, last):
    # setting pivot as first element
    pivot = array[first]
    # indexing first and last element
    i = first
    j = last
    # until i and j elements cross each other swap function set pivot
    while i < j:
        # increment i element until finds an element greater than pivot
        while i <= last and array[i] <= pivot:
            i += 1
        # decrement j element until finds an element less than pivot
        while j >= first and array[j] > pivot:
            j -= 1
        if i < j:
            swap(array, i, j)

    swap(array, first, j)
    return j


def quick_sort(array, first, last):
    if first < last:
        # p is pivot index after partitioning
        p = partition(array, first, last)
        # recursively sort, left and right of pivot
        quick_sort(array, first, p - 1)
        quick_sort(array, p + 1, last)


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
    print(f"Time complexity for quick sort {t_end-t_start}")
