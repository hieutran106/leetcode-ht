import unittest
from .solution import Solution
from utils.my_tree import create_tree_from_array

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        root = create_tree_from_array([5,3,6,2,4,None,7])
        actual = self.s.findTarget(root, 9)
        self.assertEqual(True, actual)

    def test_case2(self):
        root = create_tree_from_array([5,3,6,2,4,None,7])
        actual = self.s.findTarget(root, 28)
        self.assertEqual(False, actual)

    def test_case3(self):
        root = create_tree_from_array([2, 1, 3])
        actual = self.s.findTarget(root, 4)
        self.assertEqual(True, actual)

    def test_case4(self):
        root = create_tree_from_array([2, 1, 3])
        actual = self.s.findTarget(root, 3)
        self.assertEqual(True, actual)


if __name__ == '__main__':
    unittest.main()

