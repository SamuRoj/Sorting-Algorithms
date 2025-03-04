# Insertion Sort

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while arr[j] > key and j >= 0:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        
# Bubble Sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swap = False
        for j in range(1, n - i):
            if arr[j-1] > arr[j]:
                swap = True
                arr[j-1], arr[j] = arr[j], arr[j-1]
        if not(swap):
            break

# Selection Sort

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        minIndex = i
        for j in range(i + 1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]

# Merge Sort

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        # Dividing into smaller arrays by halves
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        # Indexes for the subarrays
        i = j = 0
        k = left

        # Creating new temporary subarrays within the given range
        leftArr = arr[left: mid + 1]
        rightArr = arr[mid + 1:right + 1]

        # Swapping the values into their proper positions
        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] < rightArr[j]:
                arr[k] = leftArr[i]
                i += 1
            else: 
                arr[k] = rightArr[j]
                j += 1
            k += 1

        # Appending the remaining elements of the arrays
        while i < len(leftArr):
            arr[k] = leftArr[i]
            i += 1
            k += 1
        while j < len(rightArr):
            arr[k] = rightArr[j]
            j += 1
            k += 1

# Quick Sort

def partition(arr, left, right):
    pivot = arr[left]
    i = right + 1
    for j in range(right, left - 1, -1):
        if arr[j] > pivot:
            i -= 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i-1], arr[left] = arr[left], arr[i-1]
    return i - 1

def quick_sort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        quick_sort(arr, left, pivot - 1)
        quick_sort(arr, pivot + 1, right)