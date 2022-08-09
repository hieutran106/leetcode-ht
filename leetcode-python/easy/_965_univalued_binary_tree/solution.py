from utils.my_tree import TreeNode


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root is None:
            return False

        return self.helper(root, root.val)

    def helper(self, node: TreeNode, value: int) -> bool:
        if node is None:
            return True
        if node.val != value:
            return False
        # check left and right
        return self.helper(node.right, value) and self.helper(node.left, value)



