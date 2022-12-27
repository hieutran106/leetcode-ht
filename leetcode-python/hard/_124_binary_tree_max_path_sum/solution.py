from typing import Optional, Tuple

from utils.my_tree import TreeNode


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        max_connect, max_value = self.max_node(root)

        return max_value

    def max_node(self, node: TreeNode) -> Tuple[int, int]:
        if not node.left and not node.right:
            return node.val, node.val

        left_max_connect, left_max_value  = 0, -1001
        if node.left:
            left_max_connect, left_max_value = self.max_node(node.left)

        right_max_connect, right_max_value = 0, -1001
        if node.right:
            right_max_connect, right_max_value = self.max_node(node.right)

        max_connect = max([left_max_connect + node.val, node.val, right_max_connect + node.val])
        max_value = max([left_max_value, right_max_value, left_max_connect + node.val + right_max_connect, max_connect])
        return max_connect, max_value




