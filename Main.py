"""
Name: Ramazan Karkin
Student ID : 150119512

"""
import time
import math


# 1. Insertion-sort
def insertion_sort(array):
    counter = 0
    # traversing from 1 to size of list.
    for index in range(1, len(array)):

        value = array[index]

        position = index

        # carry list of elements to the right which larger than trying to insert
        while position > 0 and array[position - 1] > value:
            counter += 1
            array[position] = array[position - 1]
            position -= 1
        array[position] = value

    return array


# 2. Binary Insertion-sort
def binaryinsertion_sort(array):
    for index in range(1, len(array)):
        value = array[index]
        pos = binary_search(array, value, 0, index - 1)
        for j in range(index, pos, -1):
            array[j] = array[j - 1]
        array[pos] = value
    return array


def binary_search(array, key, first, last):
    if first > last:
        return first
    # find middle element
    middle = (first + last) // 2

    if key < array[middle]:
        # if key smaller than middle, then it is in left sublist
        return binary_search(array, key, first, middle - 1)
        # else the key is in right sublist
    else:
        return binary_search(array, key, middle + 1, last)


# 3. Merge-sort
def merge(array, left, middle, right):
    n1 = middle - left + 1
    n2 = right - middle
    # create temp lists
    L = [None for _ in range(n1)]
    R = [None for _ in range(n2)]
    # copy elements to temp lists
    for i in range(0, n1):
        L[i] = array[left + i]
    for j in range(0, n2):
        R[j] = array[middle + 1 + j]

    # initial indexes fro merged lists
    i, j, k = 0, 0, left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1
    # remaining elements of L[] copy
    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1
    # remaining elements of R[] copy
    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1


# sort function which sorts array[from l to r] using function merge()
def merge_sort(array, left, right):
    if left < right:
        # find middle point
        middle = (left + right - 1) // 2
        merge_sort(array, left, middle)
        merge_sort(array, middle + 1, right)
        merge(array, left, middle, right)
    return array


# 4. Quick-sort
# pass index of array to swap
def swap1(array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp


def partition1(array, first, last):
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
            swap1(array, i, j)

    swap1(array, first, j)
    return j


def quick_sort(array, first, last):
    if first < last:
        # p is pivot index after partitioning
        p = partition1(array, first, last)
        # recursively sort, left and right of pivot
        quick_sort_MOT(array, first, p - 1)
        quick_sort_MOT(array, p + 1, last)

    return array


# 5. Quick-sort with median-of-three pivot selection

# pass index of array to swap
def swap2(array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp


# find partition position
def partition2(array, first, last):
    # setting pivot as median of three element
    pivot = median_of_three(array, first, last)
    # indexing of smaller element
    i = first - 1
    # traverse all elements compare each of elements with pivot
    for j in range(first, last):
        if array[j] <= pivot:
            i += 1
            swap2(array, i, j)
    # swapping the pivot with the greater element
    swap2(array, i + 1, last)
    return i + 1


def quick_sort_MOT(array, first, last):
    if first < last:
        # p is pivot index after partitioning
        p = partition2(array, first, last)
        # recursively sort, left and right of pivot
        quick_sort_MOT(array, first, p - 1)
        quick_sort_MOT(array, p + 1, last)
    return array


def median_of_three(array, left, right):
    mid = math.ceil((left + right) / 2)
    if array[left] > array[mid]:
        swap2(array, left, mid)
    if array[left] > array[right]:
        swap2(array, left, right)
    if array[mid] > array[right]:
        swap2(array, mid, right)
    swap2(array, mid, right)
    return array[right]


# 6. Heap-sort
def heap_sort(array):
    n = len(array)
    # building max heap
    for i in range(n // 2 - 1, -1, -1):
        heap(array, n, i)
    # heap sort
    for j in range(n - 1, 0, -1):
        # move root to end
        temp = array[0]
        array[0] = array[j]
        array[j] = temp
        # heap root element to get greatest element as a root again
        heap(array, j, 0)
    return array


def heap(array, n, i):
    # initializing largest as a root and initialize children
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[left] > array[largest]:
        largest = left
    if right < n and array[right] > array[largest]:
        largest = right
    # Swap if root is not largest
    if largest != i:
        swap = array[i]
        array[i] = array[largest]
        array[largest] = swap
        heap(array, n, largest)


# 7. Counting-sort

def counting_sort(array):
    max_element = int(max(array))
    min_element = int(min(array))
    range_of_elements = max_element - min_element + 1
    # Create a count array to store count of individual
    # elements and initialize count array as 0
    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(array))]

    # Store count of each character
    for i in range(0, len(array)):
        count_arr[array[i] - min_element] += 1

    # Change count_arr[i] so that count_arr[i] now contains actual
    # position of this element in output array
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    # Build the output character array
    for i in range(len(array) - 1, -1, -1):
        output_arr[count_arr[array[i] - min_element] - 1] = array[i]
        count_arr[array[i] - min_element] -= 1

    # Copy the output array to arr, so that arr now
    # contains sorted characters
    for i in range(0, len(array)):
        array[i] = output_arr[i]

    return array


def Main(mylist):
    global word
    for i in range(0, len(mylist)):
        with open(mylist[i], "r") as file:
            data = file.readlines()
        for line in data:
            word = line.split()

        word = [int(i) for i in word]
        t_first = time.time()
        counter1 = insertion_sort(word)
        t_second = time.time()
        binaryinsertion_sort(word)
        t_third = time.time()
        merge_sort(word, 0, len(word) - 1)
        t_forth = time.time()
        quick_sort(word, 0, len(word) - 1)
        t_fifth = time.time()
        quick_sort_MOT(word, 0, len(word) - 1)
        t_sixth = time.time()
        heap_sort(word)
        t_seventh = time.time()
        counting_sort(word)
        t_eighth = time.time()

        print(mylist[i].split(".")[0])

        print(f"Time complexity for Insertion-sort :{t_second - t_first}")
        print(f"Time complexity for Binary Insertion-sort: {t_third - t_second}")
        print(f"Time complexity for Merge-sort: {t_forth - t_third}")
        print(f"Time complexity for Quick-sort: {t_fifth - t_forth}")
        print(f"Time complexity for Quick-sort with MOT: {t_sixth - t_fifth}")
        print(f"Time complexity for Heap-sort: {t_seventh - t_sixth}")
        print(f"Time complexity for Counting-sort: {t_eighth - t_seventh}")
        print("")

        print("Insertion-sort: ", insertion_sort(word))
        print("Binary Insertion-sort: ", binaryinsertion_sort(word))
        print("Merge-sort: ", merge_sort(word, 0, len(word) - 1))
        print("Quick-sort: ", quick_sort(word, 0, len(word) - 1))
        print("Quick-sort with MOT: ", quick_sort_MOT(word, 0, len(word) - 1))
        print("Heap-sort: ", heap_sort(word))
        print("Counting-sort: ", counting_sort(word))
        print(" ")


mylist3 = ["random-100.txt", "random-500.txt", "random-1000.txt", "random-5000.txt", "random-10000.txt"]

mylist2 = ["reversed-100.txt", "reversed-500.txt", "reversed-1000.txt", "reversed-5000.txt", "reversed-10000.txt"]

mylist1 = ["sorted-100.txt", "sorted-500.txt", "sorted-1000.txt", "sorted-5000.txt", "sorted-10000.txt"]

inp = int(input(
    "Please Chose varius input data:\n(1) For sorted input cases: \n(2) For reversed input cases: \n(3) For random input cases:"))
if inp == 1:
    print("**************** Sorted Cases ****************")
    Main(mylist1)
elif inp == 2:
    print("**************** Reversed Cases ****************")
    Main(mylist2)
elif inp == 3:
    print("**************** Random Cases ****************")
    Main(mylist3)
