# Insertion Sort

def insertion_sort(arr):                
    for i in range(1, len(arr)):                # O(n)
        key = arr[i]                            # O(1)
        j = i - 1                               # O(1)
        while arr[j] > key and j >= 0:          # Σ (i=1 - n-1) ti
            arr[j+1] = arr[j]                   # O(1)
            j -= 1                              # O(1)
        arr[j+1] = key                          # O(1)
        
# Worst Case = n(n-1)/2 = O(n²)
# Best Case = O(n) The array is already sorted and the inner loop is skipped

# Bubble Sort

def bubble_sort(arr):
    n = len(arr)                                        # O(1)
    for i in range(n):                                  # O(n)
        swap = False                                    # O(1)
        for j in range(1, n - i):                       # Σ (i=0 - n-1) ti
            if arr[j-1] > arr[j]:                       # O(1)
                swap = True                             # O(1)
                arr[j-1], arr[j] = arr[j], arr[j-1]     # O(1)
        if not(swap):                                   # O(1)
            break                                       # O(1)

# Worst Case = n(n-1)/2 = O(n²)
# Best Case = O(2n) = O(n) The array is already sorted and the inner loop is executed once

# Selection Sort

def selection_sort(arr):
    n = len(arr)                                        # O(1)
    for i in range(n - 1):                              # O(n)
        minIndex = i                                    # O(1)
        for j in range(i + 1, n):                       # Σ (i=i+1 - n) ti
            if arr[j] < arr[minIndex]:                  # O(1)
                minIndex = j                            # O(1)
        arr[i], arr[minIndex] = arr[minIndex], arr[i]   # O(1)

# Worst Case = n(n-1)/2 = O(n²)
# Best Case = O(n²) The array is already sorted, but the algorithm is always trying to find the minimum value
# and put it in it's place. 

# Merge Sort

def merge_sort(arr, left, right):
    if left < right:                                                    # O(1)
        mid = (left + right) // 2                                       # O(1)

        # Dividing into smaller arrays by halves
        merge_sort(arr, left, mid)                                      # T(n/2)
        merge_sort(arr, mid + 1, right)                                 # T(n/2)

        # Indexes for the subarrays
        i = j = 0                                                       # O(1)
        k = left                                                        # O(1)

        # Creating new temporary subarrays within the given range
        leftArr = arr[left: mid + 1]                                    # O(n)
        rightArr = arr[mid + 1:right + 1]                               # O(n)

        # Swapping the values into their proper positions
        while i < len(leftArr) and j < len(rightArr):                   # O(n)
            if leftArr[i] < rightArr[j]:                                # O(1)
                arr[k] = leftArr[i]                                     # O(1)
                i += 1                                                  # O(1)
            else:                                                       # O(1)
                arr[k] = rightArr[j]                                    # O(1)
                j += 1                                                  # O(1)
            k += 1                                                      # O(1)

        # Appending the remaining elements of the arrays
        while i < len(leftArr):                                         # O(n)
            arr[k] = leftArr[i]                                         # O(1)
            i += 1                                                      # O(1)
            k += 1                                                      # O(1)
        while j < len(rightArr):                                        # O(n)
            arr[k] = rightArr[j]                                        # O(1)
            j += 1                                                      # O(1)
            k += 1                                                      # O(1)

# Worst Case = 2T(n/2) + O(n) = O(n * log(n)) Master Theorem
# Best Case = O(n * log(n)) The array is already sorted, but the algorithm is executed normally

# Quick Sort

def partition(arr, left, right):
    pivot = arr[left]                           # O(1)
    i = right + 1                               # O(1)
    for j in range(right, left - 1, -1):        # O(n)
        if arr[j] > pivot:                      # O(1)
            i -= 1                              # O(1)
            arr[i], arr[j] = arr[j], arr[i]     # O(1)
    arr[i-1], arr[left] = arr[left], arr[i-1]   # O(1)
    return i - 1                                # O(1)

def quick_sort(arr, left, right):
    if left < right:                            # O(1)
        pivot = partition(arr, left, right)     # O(n)                    
        quick_sort(arr, left, pivot - 1)        # T(n/2)           
        quick_sort(arr, pivot + 1, right)       # T(n/2)

# Worst Case = T(n-1) + T(0) + O(n) = O(n²) The array is already sorted and each side is unbalanced 0 <-> n-1. 
# Best Case = 2T(n/2) + O(n) = O(n * log(n)) Each side has a balance. 