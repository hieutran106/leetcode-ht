from typing import List

from utils.my_tree import TreeNode

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path = []
        self.find_path(root, p.val, p_path)

        q_path = []
        self.find_path(root, q.val, q_path)
        print(p_path)
        print(q_path)

        result = root
        for i in range(min(len(p_path), len(q_path))):
            if p_path[i] == q_path[i]:
                # go down
                if p_path[i] == 'L':
                    result = result.left
                else:
                    result = result.right
            else:
                break

        return result

    def find_path(self, node: TreeNode, val: int, path: List[str]):
        if node.val == val:
            return
        if val < node.val:
            path.append("L")
            self.find_path(node.left, val, path)
        else:
            path.append("R")
            self.find_path(node.right, val, path)