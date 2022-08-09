import unittest
from .bubble_sort import bubble_sort

class TestBubbleSort(unittest.TestCase):
    def test_case1(self):
        input = [3, 2, 1]
        actual = bubble_sort(input)
        self.assertEqual(actual, sorted(input))


    def test_case2(self):
        input = [5, 4, 3, 2, 1]
        actual = bubble_sort(input)
        self.assertEqual(actual, sorted(input))

    def test_case3(self):
        input = [0, 4, 6, 8, 4, 7, 9, 10]
        actual = bubble_sort(input)
        self.assertEqual(actual, sorted(input))

    def test_case4(self):
        input = [1]
        actual = bubble_sort(input)
        self.assertEqual(actual, sorted(input))