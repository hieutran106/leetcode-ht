import unittest
from .solution import Solution
from utils import my_tree

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        root = my_tree.create_tree_from_array([0, None, 1])
        result_root = self.s.bstToGst(root)
        self.assertEqual(result_root.val, 1)
        self.assertEqual(result_root.right.val, 1)

    def test_case2(self):
        root = my_tree.create_tree_from_array([1, 0, 2])
        result_root = self.s.bstToGst(root)
        self.assertEqual(result_root.val, 3)
        self.assertEqual(result_root.right.val, 2)
        self.assertEqual(result_root.left.val, 3)

    def test_case3(self):
        root = my_tree.create_tree_from_array([3, 2, 4, 1])
        result_root = self.s.bstToGst(root)
        self.assertEqual(result_root.val, 7)
        self.assertEqual(result_root.right.val, 4)
        self.assertEqual(result_root.left.val, 9)
        self.assertEqual(result_root.left.left.val, 10)

    def test_case4(self):
        root = my_tree.create_tree_from_array([4,1,6,0,2,5,7,None,None,None,3,None,None,None,8])
        result_root = self.s.bstToGst(root)
        self.assertEqual(result_root.val, 30)
        self.assertEqual(result_root.left.val, 36)
        self.assertEqual(result_root.left.left.val, 36)

if __name__ == '__main__':
    unittest.main()

