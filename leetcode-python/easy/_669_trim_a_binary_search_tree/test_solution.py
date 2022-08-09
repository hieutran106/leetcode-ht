import unittest
from .solution import Solution
from utils.my_tree import create_tree_from_array

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        head = create_tree_from_array([1, 0, 2])
        actual = self.s.trimBST(head, 1, 2)
        self.assertTrue(actual.left is None)

    def test_case2(self):
        head = create_tree_from_array([1])
        actual = self.s.trimBST(head, 1, 2)
        self.assertTrue(actual.val, 1)

    def test_case3(self):
        head = create_tree_from_array([1, None, 2])
        actual = self.s.trimBST(head, 1, 2)
        self.assertTrue(actual.left is None)

    def test_case4(self):
        head = create_tree_from_array([1, None, 2])
        actual = self.s.trimBST(head, 2, 3)
        self.assertEqual(actual.val, 2)

    def test_case5(self):
        root = create_tree_from_array([3, 0, 4])
        sub = create_tree_from_array([2, 1])
        # merge
        root.left.right = sub
        actual = self.s.trimBST(root, 1, 3)
        self.assertEqual(root.val, 3)
        self.assertEqual(root.left.val, 2)
        self.assertTrue(root.left.right is None)
        self.assertEqual(root.left.left.val, 1)



if __name__ == '__main__':
    unittest.main()

