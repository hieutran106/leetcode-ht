import unittest
from .solution import Solution
from utils.my_tree import TreeNode, deserialize

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        root = deserialize("5,4,8,11,null,13,4,7,2,null,null,null,1")
        actual = self.s.hasPathSum(root, 22)
        self.assertEqual(actual, True)

    def test_case_2(self):
        root = deserialize("1,2,3")
        actual = self.s.hasPathSum(root, 5)
        self.assertEqual(actual, False)

    def test_case_3(self):
        root = None
        actual = self.s.hasPathSum(root, 0)
        self.assertEqual(actual, False)


if __name__ == '__main__':
    unittest.main()

