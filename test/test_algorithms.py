import unittest
import random

from sorting import algorithms
from sorting import data_generator
from sorting import constants

arrays = [
    [i for i in range(8, 27)],
    [i for i in range(35, 55)],
    [i for i in range(55, 75)],
    [i for i in range(100, 130)],
    [i for i in range(50, 233)],
    [i for i in range(170, 200)],
    [i for i in range(120, 150)],
    [i for i in range(80, 110)],
    [i for i in range(300, 349)],
    [i for i in range(50, 80)],
    [i for i in range(25, 55)],
    [i for i in range(1, 180)],
    [i for i in range(185, 215)],
    [i for i in range(221, 530)],
    [i for i in range(3, 290)]
]

expected = [
    [i for i in range(8, 27)],
    [i for i in range(35, 55)],
    [i for i in range(55, 75)],
    [i for i in range(100, 130)],
    [i for i in range(50, 233)],
    [i for i in range(170, 200)],
    [i for i in range(120, 150)],
    [i for i in range(80, 110)],
    [i for i in range(300, 349)],
    [i for i in range(50, 80)],
    [i for i in range(25, 55)],
    [i for i in range(1, 180)],
    [i for i in range(185, 215)],
    [i for i in range(221, 530)],
    [i for i in range(3, 290)]
]

class AlgorithmsTests(unittest.TestCase):
    def test_insertion_sort(self):
        for i in range(len(arrays)):
            random.shuffle(arrays[i])
            array = arrays[i]
            algorithms.insertion_sort(array)
            self.assertEqual(array, expected[i])

    def test_bubble_sort(self):
        for i in range(len(arrays)):
            random.shuffle(arrays[i])
            array = arrays[i]
            algorithms.bubble_sort(array)
            self.assertEqual(array, expected[i])

    def test_selection_sort(self):
        for i in range(len(arrays)):
            random.shuffle(arrays[i])
            array = arrays[i]
            algorithms.selection_sort(array)
            self.assertEqual(array, expected[i])

    def test_merge_sort(self):
        for i in range(len(arrays)):
            random.shuffle(arrays[i])
            array = arrays[i]
            algorithms.merge_sort(array, 0, len(array) - 1)
            self.assertEqual(array, expected[i])

    def test_quick_sort(self):
        for i in range(len(arrays)):
            random.shuffle(arrays[i])
            array = arrays[i]
            algorithms.quick_sort(array, 0, len(array) - 1)
            self.assertEqual(array, expected[i])

if __name__ == "__main__":
    unittest.main()
