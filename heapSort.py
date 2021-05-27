import time
def sort(list):
    n = len(list)
    # building max heap
    for i in range(n // 2 - 1, -1, -1):
        heap(list, n, i)
    # heap sort
    for j in range(n - 1, 0, -1):
        # move root to end
        temp = list[0]
        list[0] = list[j]
        list[j] = temp
        # heap root element to get greatest element as a root again
        heap(list, j, 0)


def heap(list, n, i):
    # initializing largest as a root and initialize children
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and list[left] > list[largest]:
        largest = left
    if right < n and list[right] > list[largest]:
        largest = right
    # Swap if root is not largest
    if largest != i:
        swap = list[i]
        list[i] = list[largest]
        list[largest] = swap
        heap(list, n, largest)


with open("reversed_100.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)

    word = [int(i) for i in word]
    t_start = time.time()
    sort(word)
    t_end = time.time()
    print("Sorted array is:")
    for i in range(len(word)):
        print(word[i], end=" ")
    print("")
    print(f"Time complexity for quick sort {t_end-t_start}")
