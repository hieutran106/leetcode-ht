import unittest
from typing import List, Optional
from utils.my_tree import TreeNode, deserialize


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def helper(node: TreeNode, level: int):
            if node is None:
                return None, level
            l_val, l_level = helper(node.left, level + 1)
            r_val, r_level = helper(node.right, level + 1)
            if l_val is None and r_val is None:
                return node.val, level
            if l_val is None:
                return r_val, r_level
            if r_val is None:
                return l_val, l_level
            if l_level >= r_level:
                return l_val, l_level
            else:
                return r_val, r_level

        val, level = helper(root, 0)
        return val


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        root = deserialize("2,1,3")
        actual = self.s.findBottomLeftValue(root)
        self.assertEqual(actual, 1)

    def test_case_2(self):
        root = deserialize("1,2,3,4,null,5,6,null,null,7")
        actual = self.s.findBottomLeftValue(root)
        self.assertEqual(actual, 7)

    def test_case_3(self):
        root = deserialize("1,2,3,4,null,5,6")
        actual = self.s.findBottomLeftValue(root)
        self.assertEqual(actual, 4)

    def test_case_4(self):
        root = deserialize("6,7,3,4,null,5,6,null,null,null,null,null,7")
        actual = self.s.findBottomLeftValue(root)
        self.assertEqual(actual, 7)


if __name__ == '__main__':
    unittest.main()
