import time
def counting_sort(array):
    n = len(array)
    count = [0] * n
    s = [0] * n

    for i in range(0, n):
        j = i + 1
        while j > i and j < n:
            if array[i] < array[j]:
                count[j] = count[j] + 1
            else:
                count[i] = count[i] + 1

            j += 1

    for k in range(0, n):
        s[count[k]] = array[k]




with open("reversed_100.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)

    word = [int(i) for i in word]
    t_start = time.time()
    counting_sort(word)
    t_end = time.time()
    print("Sorted array is:")
    for i in range(len(word)):
        print(word[i], end=" ")
    print("")
    print(f"Time complexity for quick sort {t_end-t_start}")
