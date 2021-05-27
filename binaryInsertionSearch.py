import time


def insertion_sort(array):
    for index in range(1, len(array)):
        value = array[index]
        pos = binary_search(array, value, 0, index - 1)



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



with open("sorted_500.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)

    word = [int(i) for i in word]
    t_start = time.time()
    insertion_sort(word)
    t_end = time.time()
    print("Sorted array is:")
    for i in range(len(word)):
        print(word[i], end=" ")
    print("")
    print(f"Time complexity for quick sort {t_end - t_start}")
