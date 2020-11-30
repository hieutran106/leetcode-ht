import unittest
from .solution import Solution
from utils.my_list import createListFromArray, createArrayFromList

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        l1 = createListFromArray([2, 4, 3])
        l2 = createListFromArray([5, 6, 4])
        actual = self.s.addTwoNumbers(l1, l2)
        actual_array = createArrayFromList(actual)
        self.assertEqual([7, 0, 8], actual_array)

    def test_case2(self):
        l1 = createListFromArray([0])
        l2 = createListFromArray([0])
        actual = self.s.addTwoNumbers(l1, l2)
        actual_array = createArrayFromList(actual)
        self.assertEqual([0], actual_array)

    def test_case3(self):
        l1 = createListFromArray([9,9,9,9,9,9,9])
        l2 = createListFromArray([9,9,9,9])
        actual = self.s.addTwoNumbers(l1, l2)
        actual_array = createArrayFromList(actual)
        self.assertEqual([8,9,9,9,0,0,0,1], actual_array)

    def test_case4(self):
        l1 = createListFromArray([5, 5, 5])
        l2 = createListFromArray([7])
        actual = self.s.addTwoNumbers(l1, l2)
        actual_array = createArrayFromList(actual)
        self.assertEqual([2, 6, 5], actual_array)



if __name__ == '__main__':
    unittest.main()

