import unittest
from typing import List, Optional
from utils.my_tree import TreeNode, deserialize


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(node: TreeNode, visit: List[int]):
            if node is None:
                return
            visit.append(node.val)
            helper(node.left, visit)
            helper(node.right, visit)

        ans = []
        helper(root, ans)
        return ans


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        root = deserialize("1,null,2,3")
        actual = self.s.preorderTraversal(root)
        self.assertEqual(actual, [1, 2, 3])

    def test_case_2(self):
        root = deserialize("1,2,3,4,5,null,8,null,null,6,7,9")
        actual = self.s.preorderTraversal(root)
        self.assertEqual(actual, [1, 2, 4, 5, 6, 7, 3, 8, 9])

    def test_case_2(self):
        root = None
        actual = self.s.preorderTraversal(root)
        self.assertEqual(actual, [])


if __name__ == '__main__':
    unittest.main()
