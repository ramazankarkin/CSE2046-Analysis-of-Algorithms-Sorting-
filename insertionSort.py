"""
Name: Ramazan Karkin
Student ID : 150119512

"""
import time


def insertion_sort(list):
    # traversing from 1 to size of list.
    counter = 0
    for index in range(1, len(list)):
        value = list[index]

        position = index

        # carry list of elements to the right which larger than trying to insert
        while position > 0 and list[position - 1] > value:
            counter += 1
            list[position] = list[position - 1]
            position -= 1
        list[position] = value
    print("counter value is:", counter)




arr = [12, 11, 13, 5, 6,78,4,12,75,45,12]
insertion_sort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i])


""""
with open("reversed_100.txt", "r") as file:
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
    print(f"Time complexity for insertion sort {t_end-t_start}")
"""
