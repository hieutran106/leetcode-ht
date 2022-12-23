from typing import Optional, Tuple

from utils.my_tree import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        diameter, _ = self.helper(root)
        return diameter

    def helper(self, node: TreeNode) -> Tuple[int, int]:
        """
        Return both diameter and height from the input node
        """
        l = node.left
        r = node.right
        if l is None and r is None:
            return (0, 0)
        if l is not None and r is None:
            l_d, l_h = self.helper(l)
            h = l_h + 1
            d = max(l_d, h)
            return d, h
        if l is None and r is not None:
            r_d, r_h = self.helper(r)
            h = r_h + 1
            d = max(r_d, h)
            return d, h

        l_d, l_h = self.helper(l)
        r_d, r_h = self.helper(r)
        h = max(l_h, r_h) + 1
        d = max(l_d, r_d, l_h + r_h + 2)
        return d, h
