# Course: CSCI 356, Section 1
# Student Name: Ethan Zawada
# Student ID: 10627257
# Program 7
# Due Date: 4/8/22
# In keeping with the Honor Code of UM, I have neither given nor received inappropriate assistance
# from anyone other than the TA or the instructor.
# Program Description: This program performs a selection, bubble, insertion, merge, and quick sort
# on a list of data, and shows each step of the sorts on screen.

# selection sort function
def selectionSort(array, size):
    count = 1

    # iterate through the size of the array
    for i in range(size):
        # find the minimum element
        min_idx = i
        for j in range(i + 1, size):
            if array[j] < array[min_idx]:
                min_idx = j

        # swap min element with the first
        (array[i], array[min_idx]) = (array[min_idx], array[i])
        # print steps
        print('Pass ' + str(count) + ': ' + str(array))
        count += 1

# bubble sort function
def bubbleSort(array):
    count = 1
    n = len(array)

    # iterate through the array
    for i in range(n):

        # the last i elements are in correct position
        for j in range(0, n - i - 1):

            # iterate through, swapping if the element found is greater than the next
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
        # print the steps
        print('Pass ' + str(count) + ': ' + str(array))
        count += 1

# insertion sort function
def insertionSort(array):
    count = 1
    # iterate through 1 to the length of the array
    for i in range(1, len(array)):
        key = array[i]

        j = i - 1
        # compare the key with each element on the left of it until
        # a smaller one is found
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1

        # position the key after the element that is smaller
        array[j + 1] = key
        # print steps
        print('Pass ' + str(count) + ': ' + str(array))
        count += 1

# merge sort function
def mergeSort(array):
    # print when splitting
    print("Splitting", array)
    if len(array) > 1:

        # find the mid of the array
        mid = len(array) // 2
        # divide the array elements into halves
        L = array[:mid]
        R = array[mid:]

        # sort the two halves
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        # copy the data to temporary arrays
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        # check if any element on the left or right
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1
    # print when merging
    print("Merging", array)


def partition(array, start, end):
    # pivot
    pivot = array[start]
    print('Pivot value: ' + str(pivot))
    # index of smaller element
    low = start + 1
    high = end

    while True:
        # if the value is larger than the pivot it is in the right position
        # now move left to next element
        # also check it hasn't passed the lower index
        while low <= high and array[high] >= pivot:
            high = high - 1

        # the opposite of the above
        while low <= high and array[low] <= pivot:
            low = low + 1

        # this either finds a value for high and low that is not in the correct
        # position, or a low higher than the high, this breaks the loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]
    # print list after partitioning
    print('List after partition: ' + str(array))

    return high


# function to perform quicksort
def quickSort(array, start, end):
    if start >= end:
        return
    # partitioning
    p = partition(array, start, end)
    # sort elements before and after partition
    quickSort(array, start, p - 1)
    quickSort(array, p + 1, end)


# main function to call all the other sorts and print to screen
def main():
    data = [19, 1, 9, 7, 3, 10]
    size = len(data)

    print('Selection Sort')
    selectionSort(data, size)
    print()

    print('Bubble Sort')
    data = [19, 1, 9, 7, 3, 10]
    bubbleSort(data)
    print()

    print('Insertion Sort')
    data = [19, 1, 9, 7, 3, 10]
    insertionSort(data)
    print()

    print('Merge Sort')
    data = [5, 1, 4, 2, 3]
    mergeSort(data)
    print()

    print('Quick Sort')
    data = [5, 1, 4, 2, 3]
    quickSort(data, 0, size - 1)

main()