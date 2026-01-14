import collections
import unittest
from typing import List, Optional
from utils.my_tree import TreeNode, deserialize
# Date: 2026-01-06
# Problem: 1181 max_level_sum_binary_tree
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_sum = collections.defaultdict(int)
        def helper(node: TreeNode, level: int):
            if node is None:
                return
            level_sum[level] += node.val
            helper(node.left, level + 1)
            helper(node.right, level + 1)

        helper(root, 1)
        print(level_sum)
        ans = float("-inf")
        max_level_sum = float("-inf")
        for k, v in level_sum.items():
            if v > max_level_sum:
                max_level_sum = v
                ans = k

        return ans
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        root = deserialize("1,7,0,7,-8,null,null")
        actual = self.s.maxLevelSum(root)
        self.assertEqual(2, actual)
        
    def test_case_2(self):
        root = deserialize("989,null,10250,98693,-89388,null,null,null,-32127")
        actual = self.s.maxLevelSum(root)
        self.assertEqual(2, actual)

    def test_case_3(self):
        root = deserialize("10,-2,-5")
        actual = self.s.maxLevelSum(root)
        self.assertEqual(1, actual)

    def test_case_4(self):
        root = deserialize("1,5,5,15")
        actual = self.s.maxLevelSum(root)
        self.assertEqual(3, actual)

if __name__ == '__main__':
    unittest.main()

