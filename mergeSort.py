import time

def merge(array, left, middle, rigth):
    n1 = middle - left + 1
    n2 = rigth - middle
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

#sort function which sorts array[from l to r] using function merge()
def sort(array, left, right):
    if left < right:
        #find middle point
        middle = (left + right - 1) // 2
        sort(array, left, middle)
        sort(array, middle + 1, right)
        merge(array, left, middle, right)




with open("reversed_100.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)

    word = [int(i) for i in word]
    t_start = time.time()
    sort(word, 0, len(word)-1)
    t_end = time.time()
    print("Sorted array is:")
    for i in range(len(word)):
        print(word[i], end=" ")
    print("")
    print(f"Time complexity for merge sort {t_end-t_start}")
