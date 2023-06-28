import unittest
from typing import Optional, List
from .solution import Solution
from utils.my_tree import TreeNode, serialize


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}

        def full_binary_tree(n: int):
            if n == 1:
                return [TreeNode(0)]
            elif n == 2:
                return []
            if n in memo:
                return memo[n]

            res = []
            for i in range(1, n - 1):
                left: List[TreeNode] = full_binary_tree(i)
                if not left:
                    continue
                right: List[TreeNode] = full_binary_tree(n - 1 - i)
                if not right:
                    continue
                for l_tree in left:
                    for r_tree in right:
                        solution = TreeNode(0, l_tree, r_tree)
                        res.append(solution)
            memo[n] = res
            return res

        return full_binary_tree(n)


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        tree_nodes = self.s.allPossibleFBT(n=3)
        data = []
        for root in tree_nodes:
            data.append(serialize(root))

        self.assertEqual(data, ['0,0,0'])

    def test_case_2(self):
        tree_nodes = self.s.allPossibleFBT(n=7)
        data = []
        for root in tree_nodes:
            data.append(serialize(root))
        expected_trees = [
            "0,0,0,null,null,0,0,null,null,0,0",
            "0,0,0,null,null,0,0,0,0",
            "0,0,0,0,0,0,0",
            "0,0,0,0,0,null,null,null,null,0,0",
            "0,0,0,0,0,null,null,0,0"
        ]
        for node in expected_trees:
            self.assertIn(node, data)


if __name__ == '__main__':
    unittest.main()
