import unittest
from typing import List


def quick_sort(array: List[int], low: int, high: int):
    if low >= high or low < 0:
        return
    # Partition array and get the pivot index
    p = lomuto_partition(array, low, high)
    # sort the two partitions
    quick_sort(array, low, p - 1)
    quick_sort(array, p +1, high)



def lomuto_partition(arr: List[int], low: int, high: int) -> int:
    """
    Lomuto partition scheme
    """
    pivot = arr[high]  # Choosing the last element as the pivot
    i = low  # Pointer for the smaller element
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i] # Swap
            i += 1 # Increment index of smaller element
    # Swap the pivot element with the element at i
    arr[i], arr[high] = arr[high], arr[i]
    return i


class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        array = [9, 6, 7, 4, 5, 8]
        quick_sort(array, 0 , len(array) - 1)
        self.assertEqual(array, [4, 5, 6, 7, 8, 9])


if __name__ == '__main__':
    unittest.main()
