from typing import List

from utils.my_tree import TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0

        result = []
        self.helper(root, -10e4 - 1, result)
        return len(result)

    def helper(self, node: TreeNode, max_value: int, result: List[int]):
        if node.val >= max_value:
            print(f"Node {node.val} is good node.")
            result.append(node.val)
        max_value = max(node.val, max_value)
        if node.left:
            self.helper(node.left, max_value, result)
        if node.right:
            self.helper(node.right, max_value, result)
