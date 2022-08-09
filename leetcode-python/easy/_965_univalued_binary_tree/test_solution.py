import unittest
from .solution import Solution
from utils.my_tree import create_tree_from_array

class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        s = Solution()
        root = create_tree_from_array([1,1,1,1,1,None,1])
        actual = s.isUnivalTree(root)
        self.assertEqual(True, actual)

    def test_case_2(self):
        s = Solution()
        root = create_tree_from_array([2,2,2,5,2])
        actual = s.isUnivalTree(root)
        self.assertEqual(False, actual)

    def test_case_3(self):
        s = Solution()
        root = create_tree_from_array([1])
        actual = s.isUnivalTree(root)
        self.assertEqual(True, actual)

    def test_case_4(self):
        s = Solution()
        root = create_tree_from_array([1, 1, 1])
        actual = s.isUnivalTree(root)
        self.assertEqual(True, actual)

    def test_case_5(self):
        s = Solution()
        root = create_tree_from_array([1, 1, 2])
        actual = s.isUnivalTree(root)
        self.assertEqual(False, actual)

    def test_case_6(self):
        s = Solution()
        root = create_tree_from_array([1, 1, 1, 2])
        actual = s.isUnivalTree(root)
        self.assertEqual(False, actual)

    def test_case_7(self):
        s = Solution()
        root = create_tree_from_array([1, 1, 1, None, 2])
        actual = s.isUnivalTree(root)
        self.assertEqual(False, actual)

if __name__ == '__main__':
    unittest.main()
