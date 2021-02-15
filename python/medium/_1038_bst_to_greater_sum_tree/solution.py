# tags: dfs, bst
from utils.my_tree import TreeNode


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.dfs(root, 0)
        return root

    def dfs(self, node: TreeNode, greater_value) -> int:
        if node is None:
            return greater_value

        right = self.dfs(node.right, greater_value)
        node.val += right
        left = self.dfs(node.left, node.val)
        return left