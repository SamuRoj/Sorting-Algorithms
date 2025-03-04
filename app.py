import sys
from sorting import algorithms
from sorting import execution_time_gathering

if __name__ == "__main__":
    minimum_size = 1000
    maximum_size = 10000
    step = 1000
    samples_by_size = 5
    
    table = execution_time_gathering.take_execution_time(minimum_size, maximum_size, step, samples_by_size)

    print("Size | Insertion Sort | Bubble Sort | Selection Sort | Merge Sort | Quick Sort")
    for row in table:
        print(row)
