import unittest
from .solution import Solution
from utils.my_list import createArrayFromList, createListFromArray

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        root = createListFromArray([1, 2, 3, 4])
        actual = self.s.reverseList(root)
        actual_array = createArrayFromList(actual)
        self.assertEqual([4, 3, 2, 1], actual_array)

    def test_case2(self):
        root = createListFromArray([1])
        actual = self.s.reverseList(root)
        actual_array = createArrayFromList(actual)
        self.assertEqual([1], actual_array)

if __name__ == '__main__':
    unittest.main()

