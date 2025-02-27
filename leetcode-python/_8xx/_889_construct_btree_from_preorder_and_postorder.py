import unittest
from typing import List, Optional

from utils.my_tree import TreeNode, serialize


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def construct(preorder: List[int], postorder: List[int]):
            if not preorder:
                return None
            root = TreeNode(preorder[0])
            if len(preorder) == 1:
                return root

            root_left_idx = None
            for i in range(0, len(postorder)):
                if postorder[i] == preorder[1]:
                    root_left_idx = i
                    break
            # print(f"{root_left_idx=}")
            # print(f"Construct left tree from preorder [{1}: {root_left_idx + 2}] - postorder[:{root_left_idx + 1}]", )
            # print(f"Which is preorder: {preorder[1: root_left_idx + 2]}, postorder: {postorder[:root_left_idx + 1]}")
            root.left = construct(preorder[1: root_left_idx + 2], postorder[:root_left_idx + 1])
            root.right = construct(preorder[root_left_idx + 2:], postorder[root_left_idx + 1: -1])
            return root

        return construct(preorder, postorder)


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.constructFromPrePost(preorder=[1, 2, 4, 5, 3, 6, 7], postorder=[4, 5, 2, 6, 7, 3, 1])
        tree_str = serialize(actual)
        self.assertEqual("1,2,3,4,5,6,7", tree_str)

    def test_case_2(self):
        actual = self.s.constructFromPrePost(preorder=[1], postorder=[1])
        tree_str = serialize(actual)
        self.assertEqual("1", tree_str)

    def test_case_3(self):
        actual = self.s.constructFromPrePost(preorder=[1, 2, 5, 3, 4], postorder=[5, 2, 4, 3, 1])
        tree_str = serialize(actual)
        self.assertEqual("1,2,3,5,null,4", tree_str)


if __name__ == '__main__':
    unittest.main()
