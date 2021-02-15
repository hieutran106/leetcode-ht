# tags: dfs

from typing import List

from utils.my_tree import TreeNode


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        result = []
        path = ""
        self.dfs(root, result, path)
        return result

    def dfs(self, node: TreeNode, result, path: str):
        if node is None:
            return

        path = path + str(node.val)
        if (node.left is None) and (node.right is None):
            result.append(path)
            return

        if node.left is not None:
            self.dfs(node.left, result, path + "->")

        if node.right is not None:
            self.dfs(node.right, result, path + "->")



