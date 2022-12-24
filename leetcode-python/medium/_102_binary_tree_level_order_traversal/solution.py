from typing import Optional, List, Deque, Tuple
from utils.my_tree import TreeNode
from collections import deque

def height(root: TreeNode) -> int:
    if root is None:
        return 0
    l_height = height(root.left)
    r_height = height(root.right)
    return max(l_height, r_height) + 1

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []

        h = height(root)
        result = [[] for _ in range(h)]
        queue = deque() # (TreeNode, int)

        queue.append((root, 1))
        while queue:
            node, h = queue.popleft()
            result[h-1].append(node.val)
            if node.left:
                queue.append((node.left, h + 1))
            if node.right:
                queue.append((node.right, h + 1))

        return result




    def helper(self, node: TreeNode, level, height):
        pass
