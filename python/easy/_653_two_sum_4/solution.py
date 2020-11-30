from utils.my_tree import TreeNode


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        residual = {}
        return self.helper(root, residual, k)

    def helper(self, node: TreeNode, residual, k:int) -> bool:
        if node is None:
            return False

        if residual.get(node.val) is not None:
            return True

        # put in residual cache
        residual[k - node.val] = True
        left = self.helper(node.left, residual, k)
        right = self.helper(node.right, residual, k)
        return left or right

