from typing import List

from utils.my_tree import TreeNode

class Codec:
    def serialize(self, root):
        if root is None:
            return ""

        q = [root]
        result = []
        while len(q) > 0:
            current_node = q.pop(0)
            if current_node is None:
                result.append(None)
            else:
                result.append(current_node.val)
                q.append(current_node.left)
                q.append(current_node.right)

        # Remove trailing None
        while result[-1] is None:
            result.pop()

        stringResult = ",".join(map(lambda x: "null" if x is None else str(x), result))
        return stringResult

    def deserialize(self, data: str):
        if data == "":
            return None

        queue: List[int] = list(map(lambda x: int(x) if x != "null" else None, data.split(",")))
        root = TreeNode(queue.pop(0))
        tree_queue: List[TreeNode] = [root]

        while len(tree_queue) > 0:
            parent = tree_queue.pop(0)
            left = queue.pop(0) if len(queue) >0 else None
            if left is not None:
                left_node = TreeNode(left)
                parent.left = left_node
                tree_queue.append(left_node)

            right = queue.pop(0) if len(queue) >0 else None
            if right is not None:
                right_node = TreeNode(right)
                parent.right = right_node
                tree_queue.append(right_node)

        return root
