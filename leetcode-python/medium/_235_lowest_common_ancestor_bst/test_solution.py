import unittest
from .solution import Solution
from utils.my_tree import serialize, deserialize

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        root = deserialize("6,2,8,0,4,7,9,null,null,3,5")
        p = root.left
        q = root.right
        actual = self.s.lowestCommonAncestor(root, p, q)
        self.assertEqual(6, actual.val)

    def test_case_2(self):
        root = deserialize("6,2,8,0,4,7,9,null,null,3,5")
        p = root.left
        q = root.left.right
        actual = self.s.lowestCommonAncestor(root, p, q)
        self.assertEqual(2, actual.val)

    def test_case_3(self):
        root = deserialize("2,1")
        p = root
        q = root.left
        actual = self.s.lowestCommonAncestor(root, p, q)
        self.assertEqual(2, actual.val)


if __name__ == '__main__':
    unittest.main()

