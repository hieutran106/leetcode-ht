import unittest
from typing import List, Optional
from utils.my_tree import deserialize, TreeNode


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(node: TreeNode):
            if node is None:
                return 0, float("inf"), float("-inf")
            diff_l, min_l, max_l = helper(node.left)
            diff_r, min_r, max_r = helper(node.right)

            min_val = min(node.val, min_l, min_r)
            max_val = max(node.val, max_l, max_r)
            diff = max(abs(node.val - min_val), abs(node.val - max_val), diff_l, diff_r)
            return diff, min_val, max_val

        res, root_min, root_max = helper(root)
        return res


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        root = deserialize("8,3,10,1,6,null,14,null,null,4,7,13")
        actual = self.s.maxAncestorDiff(root)
        self.assertEqual(7, actual)

    def test_case_2(self):
        root = deserialize("1,null,2,null,0,3")
        actual = self.s.maxAncestorDiff(root)
        self.assertEqual(3, actual)

    def test_case_3(self):
        root = deserialize("1,5")
        actual = self.s.maxAncestorDiff(root)
        self.assertEqual(4, actual)


if __name__ == '__main__':
    unittest.main()
