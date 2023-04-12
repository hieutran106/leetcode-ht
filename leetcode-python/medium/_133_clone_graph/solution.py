import collections
from typing import Dict


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        factory = {}

        def bfs(node: Node):
            print(f"Process node {node.val}")
            if node.val in factory:
                return factory[node.val]
            copy = Node(node.val)
            factory[node.val] = copy
            for nei in node.neighbors:
                copy.neighbors.append(bfs(nei))
            return copy

        return bfs(node)

