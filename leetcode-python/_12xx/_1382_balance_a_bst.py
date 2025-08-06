import unittest
from typing import List, Optional
from utils.my_tree import TreeNode, deserialize, serialize


# Date: 2025-29-07
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        inorder_nodes = []
        self.inorder_traversal(root, inorder_nodes)
        # Build balance BST from inorder_nodes (a sorted array)
        root = self.sorted_array_to_bst(0, len(inorder_nodes) - 1, inorder_nodes)
        return root

    def inorder_traversal(self, node: Optional[TreeNode], inorder: List[int]):
        if not node:
            return
        self.inorder_traversal(node.left, inorder)
        inorder.append(node.val)
        self.inorder_traversal(node.right, inorder)

    def sorted_array_to_bst(self, start: int, end: int, inorder_nodes: List[int]):
        if start > end:
            return None
        mid = (start + end) // 2
        left = self.sorted_array_to_bst(start, mid -1, inorder_nodes)
        right = self.sorted_array_to_bst(mid + 1, end, inorder_nodes)
        node = TreeNode(inorder_nodes[mid], left, right)
        return node


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        root = deserialize("1,null,2,null,3,null,4,null,null")
        actual = self.s.balanceBST(root)
        actual_str = serialize(actual)
        self.assertTrue(actual_str == "2,1,3,null,null,null,4" or actual == "3,1,4,null,2")
        
    def test_case_2(self):
        root = deserialize("2,1,3")
        actual = self.s.balanceBST(root)
        actual_str = serialize(actual)
        self.assertTrue(actual_str == "2,1,3")

if __name__ == '__main__':
    unittest.main()

