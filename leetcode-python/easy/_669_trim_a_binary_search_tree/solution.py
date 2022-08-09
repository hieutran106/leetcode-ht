# tags: binary search tree
from utils.my_tree import TreeNode


class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        result = self.helper(root, low, high)

        return result

    def helper(self, node: TreeNode, low: int, high: int) -> TreeNode:
        if node is None:
            return

        if low <= node.val <= high:
            node.left = self.helper(node.left, low, high)
            node.right = self.helper(node.right, low, high)
            return node
        elif node.val < low:
            return self.helper(node.right, low, high)
        elif node.val > high:
            return self.helper(node.left, low, high)

