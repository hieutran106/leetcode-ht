from typing import Optional
from utils.my_tree import TreeNode

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        if root.left is None and root.right is None:
            return root.val == targetSum

        left = self.hasPathSum(root.left, targetSum - root.val)
        right = self.hasPathSum(root.right, targetSum - root.val)
        return left or right


