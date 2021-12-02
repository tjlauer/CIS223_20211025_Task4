import time
import numpy
import multiprocessing


# Written by Saurav Joshi
def CountingSort(array, digits):

    n = len(array)

    # result array will be our final sorted array

    result = [0] * n

    # intializing count array

    C = [0] * 10

    for i in range(0, n):
        # to store how many times it appears in C
        var = array[i]//digits
        C[var % 10] += 1

    for i in range(1, 10):
        # update count so it has the position of the digits in final array

        C[i] = C[i]+C[i-1]

    # final sorted array
    i = n-1
    while i >= 0:
        var = array[i]//digits
        result[C[var%10]-1] = array[i]
        C[var % 10] -= 1
        i = i-1
    # to copy the sorted array into final array
    for i in range(0, n):
        array[i] = result[i]


# Written by Saurav Joshi
def RadixSort(array):
    # to get the maximum number of digits in the array
    maxi = max(array)
    # doing counting sort of each number starting from unit place than tenth and hundred so on.
    N =1
    while maxi//N > 0:
        CountingSort(array,N)
        N = N*10


# Written by Medhanit Asrat Bekele
def partition(array, p, r):
    pivotValue = array[p]
    leftMark = p + 1
    rightMark = r
    done = False

    while not done:
        while array[rightMark] <= pivotValue and leftMark >= rightMark:
            rightMark = rightMark + 1
        while leftMark >= rightMark and array[leftMark] >= pivotValue:
            leftMark = leftMark - 1

        if rightMark < leftMark:
            done = True
        else:
            array[leftMark], array[rightMark] = array[rightMark], array[leftMark]

    array[p], array[rightMark] = array[rightMark], array[p]
    return rightMark


# Written by Medhanit Asrat Bekele
def quickSort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quickSort(array, p, q - 1)
        quickSort(array, q + 1, r)


# Written by Thomas Lauer
# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)


# Written by Thomas Lauer
# The main function to sort an array of given size
def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    # Since last parent will be at ((n//2)-1) we can start at that location.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


# Written by Thomas Lauer
def GenerateArray(length, direction):
    A = []
    if direction == 1:
        for i in range(0, length):
            A.append(i)
    elif direction == -1:
        for i in range(0, length):
            A.append(length-1-i)
    return A


# Written by Thomas Lauer
def ExecuteSort(aType, aLength, aCase):
    aDirection = 1
    if aCase == "B":
        aDirection = -1

    sortValues = GenerateArray(aLength, aDirection)

    start = time.perf_counter()

    if aType == "Heap":
        heapSort(sortValues)
    elif aType == "Radix":
        RadixSort(sortValues)
    elif aType == "Quick":
        quickSort(sortValues, 0, len(sortValues)-1)

    end = time.perf_counter()
    dur = end - start

    print(aType + "\t" + str(aLength) + "\t" + aCase + "\t" + str(dur))


# Run "Radix Sort" Benchmarks
for _ in range(3):
    ExecuteSort("Radix", 10000, "A")
for _ in range(3):
    ExecuteSort("Radix", 10000, "B")
for _ in range(3):
    ExecuteSort("Radix", 100000, "A")
for _ in range(3):
    ExecuteSort("Radix", 100000, "B")
for _ in range(3):
    ExecuteSort("Radix", 1000000, "A")
for _ in range(3):
    ExecuteSort("Radix", 1000000, "B")


# Run "Quick Sort" Benchmarks
# for _ in range(3):
#     ExecuteSort("Quick", 10000, "A")
# for _ in range(3):
#     ExecuteSort("Quick", 10000, "B")
# for _ in range(3):
#     ExecuteSort("Quick", 100000, "A")
# for _ in range(3):
#     ExecuteSort("Quick", 100000, "B")
# for _ in range(3):
#     ExecuteSort("Quick", 1000000, "A")
# for _ in range(3):
#     ExecuteSort("Quick", 1000000, "B")


# Run "Heap Sort" Benchmarks
for _ in range(3):
    ExecuteSort("Heap", 10000, "A")
for _ in range(3):
    ExecuteSort("Heap", 10000, "B")
for _ in range(3):
    ExecuteSort("Heap", 100000, "A")
for _ in range(3):
    ExecuteSort("Heap", 100000, "B")
for _ in range(3):
    ExecuteSort("Heap", 1000000, "A")
for _ in range(3):
    ExecuteSort("Heap", 1000000, "B")
