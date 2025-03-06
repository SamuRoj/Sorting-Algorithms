# Sorting algorithms

Simple python project that tests some searching in array algorithms, explaining how they work and comparing his complexity and efficiency.

## Problem statement
​
The sorting an array problem involves arranging the elements of a given array in a specific order. The goal is to reorder the elements so that they follow a particular sorting criteria, such as ascending or descending order.

### Input:

An array of elements (which may or may not be sorted initially).

### Output:

The sorted array in either ascending or descending order (depending on the specification).

### Example:

Input: Array = [9, 3, 1, 7, 12]

Output: [1, 3, 7, 9, 12]

## Algorithms tested

## Insertion Sort

Is a simple comparison-based sorting algorithm. It starts from the second element, compares it with the elements before it, and inserts it into the correct position among the sorted elements.

## Bubble Sort

Is another comparison-based algorithm where the array is repeatedly traversed, and adjacent elements are swapped if they are in the wrong order.

## Selection Sort

It repeatedly finds the minimum element from the unsorted part of the array and swapps it with the first unsorted element until the array is sorted. 

## Merge Sort

Is a divide-and-conquer algorithm, it divides the array into two halves, recursively sorts each half and then merges them together. 

## Quick Sort

Is another divide-and-conquer algorithm. It selects a "pivot" element from the array, partitions the array into two subarrays (one with elements smaller than the pivot and one with elements larger) and recursively sorts the subarrays. 

# Python version
Python 3.13.1
​
# Running locally and testing

* Note: This instructions are for mac. Windows or linux may require some changes. 
* A good idea for this project, is to use a virtual environment, you could set up one with: [virtualenv](https://virtualenv.pypa.io/en/latest/).
* To create the virtual environment: `virtualenv env`
* To activate it:`source env/bin/activate`
* To install dependencies: `pip3 install -r requirements.txt`
* To run unit testing: `./test.sh`
* To try a default example, run: `: ./run.sh`. In the file ./run.sh is just an example, you can modify it. Theck the `app.py` file to get to understand how it works.

# Current coverage

Make sure you have "coverage" in your requirements.txt file and run pip install. Then run `coverage run -m unittest discover` and after that run `coverage report` to get the following table:

```
Name                          Stmts   Miss  Cover
-------------------------------------------------
sorting\__init__.py               0      0   100%
sorting\algorithms.py            64      0   100%
sorting\constants.py              2      0   100%
sorting\data_generator.py         9      1    89%
test\__init__.py                  0      0   100%
test\test_algorithms.py          40      1    98%
test\test_data_generator.py      29      1    97%
-------------------------------------------------
TOTAL                           144      3    98%
```
