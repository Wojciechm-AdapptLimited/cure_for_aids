import random


# sorting an array using insertion sort algorithm
def insertion(arr):
    # iterating from index '1' to the end of the array
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        # moving elements from arr[0,...,i - 1] that are greater than temp to their next positions
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
    return arr


# sorting an array using shell sort algorithm
def shell(arr):
    index = 1
    gaps = [1]
    # creating an array of gaps using 2^k - 1 pattern
    while gaps[-1] < len(arr):
        index += 1
        gaps.append(2 ** index - 1)
    # sorting an array using insertion sort algorithm using gaps created before
    for gap in gaps[::-1]:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp


# sorting an array using selection sort algorithm
def selection(arr):
    # iterating through an entire array
    for i in range(len(arr)):
        # finding the minimum element in unsorted part of the array
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # swapping the minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]


# building a heap tree
def heapify(arr, size, index):
    # initializing root and its children
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2
    # finding if particular child exists and is larger than root
    if left < size and arr[largest] < arr[left]:
        largest = left
    if right < size and arr[largest] < arr[right]:
        largest = right
    # changing root if necessary
    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        heapify(arr, size, largest)


# sorting an array using heap sort algorithm
def heap(arr):
    # building a max heap
    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, len(arr), i)
    # extracting elements one at the time
    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


# sorting all elements in relation to the last element (pivot) using the Hoare partition scheme
def partition(arr, start, stop):
    # initializing pivot and two indices
    pivot = arr[stop]
    i = start
    j = stop
    # looping until two indices meet
    while i < j:
        # increasing and decreasing indices accordingly, until reaching the first pair of inverted elements
        while arr[i] < pivot and i <= stop:
            i += 1
        while arr[j] > pivot and j >= start:
            j -= 1
        # swapping the inverted elements
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    # returning two indices
    return i, j


# changing random element with the last one to create the pivot
def partition_random(arr, start, stop):
    rand_pivot = random.randrange(start, stop)
    arr[rand_pivot], arr[stop] = arr[stop], arr[rand_pivot]
    return partition(arr, start, stop)


# sorting an array using quick sort algorithm
def quick(arr, start, stop, pivot_type):
    while start < stop:
        # partitioning the array into the sub arrays with elements smaller and greater than pivot
        if pivot_type == 0:
            i, j = partition(arr, start, stop)
        else:
            i, j = partition_random(arr, start, stop)
        # recurring first for the smaller one of the arrays and using tail call to recur to the other
        if stop - i < j - start:
            quick(arr, i, stop, pivot_type)
            stop = j
        else:
            quick(arr, start, j, pivot_type)
            start = i
