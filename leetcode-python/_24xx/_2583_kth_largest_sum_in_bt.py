import unittest
from typing import List, Optional
from utils.my_tree import TreeNode, deserialize
import collections
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        level_sum = collections.defaultdict(int)
        def dfs(node: TreeNode, h: int):
            if node is None:
                return
            level_sum[h] = level_sum[h] + node.val
            dfs(node.left, h + 1)
            dfs(node.right, h + 1)

        dfs(root, 0)
        values = sorted(level_sum.values(), reverse=True)
        print(level_sum)
        print(values)
        if k-1 not in range(0, len(values)):
            return -1
        return values[k - 1]
class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        root = deserialize("5,8,9,2,1,3,7,4,6")
        actual = self.s.kthLargestLevelSum(root, 2)
        self.assertEqual(13, actual)
        
    def test_case_2(self):
        root = deserialize("1,2,null,3")
        actual = self.s.kthLargestLevelSum(root, 1)
        self.assertEqual(3, actual)

    def test_case_3(self):
        root = deserialize("5,8,9,2,1,3,7")
        actual = self.s.kthLargestLevelSum(root, 4)
        self.assertEqual(-1, actual)


if __name__ == '__main__':
    unittest.main()

