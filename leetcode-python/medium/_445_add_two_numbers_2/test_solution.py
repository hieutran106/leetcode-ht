import unittest

from utils.my_list import createListFromArray, createArrayFromList
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        l1 = createListFromArray([7, 2, 4, 3])
        l2 = createListFromArray([5, 6, 4])
        actual = self.s.addTwoNumbers(l1, l2)
        actual_array = createArrayFromList(actual)
        self.assertEqual([7, 8, 0, 7], actual_array)

    def test_case2(self):
        l1 = createListFromArray([0])
        l2 = createListFromArray([0])
        actual = self.s.addTwoNumbers(l1, l2)
        actual_array = createArrayFromList(actual)
        self.assertEqual([0], actual_array)


if __name__ == '__main__':
    unittest.main()

