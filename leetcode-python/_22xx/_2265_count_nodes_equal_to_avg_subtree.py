import unittest
from typing import List

from utils.my_tree import TreeNode, deserialize


# Date: 2026-09-10
# Problem: 2265 count_nodes_equal_to_avg_subtree
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:

        ans = 0
        def helper(node: TreeNode):
            nonlocal ans
            if node is None:
                return (0, 0)

            left_sum, left_count = helper(node.left)
            right_sum, right_count = helper(node.right)

            curr_sum = node.val + left_sum + right_sum
            curr_count = 1 +left_count + right_count
            if curr_sum // curr_count == node.val:
                ans += 1

            return (curr_sum, curr_count)
        helper(root)
        return ans
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        root = deserialize("4,8,5,0,1,null,6")
        actual = self.s.averageOfSubtree(root)
        self.assertEqual(5, actual)
        
    def test_case_2(self):
        root = deserialize("1")
        actual = self.s.averageOfSubtree(root)
        self.assertEqual(1, actual)

    def test_case_3(self):
        root = deserialize("1,2,10")
        actual = self.s.averageOfSubtree(root)
        self.assertEqual(2, actual)

if __name__ == '__main__':
    unittest.main()

