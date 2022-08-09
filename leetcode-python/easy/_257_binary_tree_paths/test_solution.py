import unittest
from .solution import Solution
from utils import my_tree


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        root = my_tree.create_tree_from_array([1, 2, 3, None, 5, None, None])
        actual = self.s.binaryTreePaths(root)
        self.assertEqual(actual, ["1->2->5", "1->3"])

    def test_case2(self):
        root = my_tree.create_tree_from_array([1])
        actual = self.s.binaryTreePaths(root)
        self.assertEqual(actual, ["1"])

    def test_case3(self):
        root = my_tree.create_tree_from_array([1, 2, 3])
        actual = self.s.binaryTreePaths(root)
        self.assertEqual(actual, ["1->2", "1->3"])

    def test_case4(self):
        root = my_tree.create_tree_from_array([1, None, 3])
        actual = self.s.binaryTreePaths(root)
        self.assertEqual(actual, ["1->3"])


if __name__ == "__main__":
    unittest.main()
