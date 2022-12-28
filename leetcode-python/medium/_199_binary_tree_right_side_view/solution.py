from typing import Optional, List
from collections import deque
from utils.my_tree import TreeNode

def get_height(node: TreeNode):
    if node is None:
        return 0
    l_height = get_height(node.left)
    r_height = get_height(node.right)
    return max(l_height, r_height) + 1

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue = deque()
        h = get_height(root)
        queue.append((root, 1))
        result = []
        while queue:
            node, height = queue.popleft()
            next_node, next_height = None, None
            if queue:
                next_node, next_height = queue[0]

            if next_height is None or next_height != height:
                result.append(node.val)

            if node.left:
                queue.append((node.left, height + 1))
            if node.right:
                queue.append((node.right, height + 1))

        return result
