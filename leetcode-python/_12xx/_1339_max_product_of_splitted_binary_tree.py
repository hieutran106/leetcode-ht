import unittest
from typing import List, Optional
from utils.my_tree import TreeNode, serialize, deserialize
# Date: 2026-01-08
# Problem: 1339 max_product_of_splitted_binary_tree

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10 ** 9 + 7
        def dfs(node: TreeNode):
            if node is None:
                return 0
            return node.val + dfs(node.left) + dfs(node.right)

        total_sum = dfs(root)

        ans = float("-inf")
        def helper(node: TreeNode):
            if node is None:
                return 0
            left = helper(node.left)
            right = helper(node.right)

            c1 = left * (total_sum - left)
            c2 = right * (total_sum - right)

            nonlocal ans
            ans = max(ans, c1, c2)
            return node.val + left + right
        helper(root)
        return ans % MOD



class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        root = deserialize("1,2,3,4,5,6")
        actual = self.s.maxProduct(root)
        self.assertEqual(110, actual)
        
    def test_case_2(self):
        root = deserialize("1,null,2,3,4,null,null,5,6")
        actual = self.s.maxProduct(root)
        self.assertEqual(90, actual)

    def test_case_3(self):
        with open('./_12xx/_1339_test.txt', 'r') as file:
            data = file.read().rstrip()
            root = deserialize(data)
            actual = self.s.maxProduct(root)
            self.assertEqual(763478770, actual)

if __name__ == '__main__':
    unittest.main()

