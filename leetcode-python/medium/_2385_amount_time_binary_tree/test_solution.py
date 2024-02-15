import unittest
from typing import Optional
import collections
from utils.my_tree import deserialize, TreeNode

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adjacency_map = collections.defaultdict(list)
        def build_adj_map(node: TreeNode):
            val = node.val
            if node.left is not None:
                adjacency_map[val].append(node.left.val)
                adjacency_map[node.left.val].append(val)
                build_adj_map(node.left)
            if node.right is not None:
                adjacency_map[val].append(node.right.val)
                adjacency_map[node.right.val].append(val)
                build_adj_map(node.right)
        # build graph from tree
        build_adj_map(root)
        print(adjacency_map)
        # perform dfs
        queue = [start]
        visited = set()
        time = 0
        while len(queue) > 0:
            next_queue = []
            for node in queue:
                visited.add(node)
                neighbours = adjacency_map[node]
                for n in neighbours:
                    if n not in visited:
                        next_queue.append(n)
            queue = next_queue
            time += 1

        return time - 1
class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        root = deserialize("1,5,3,null,4,10,6,9,2")
        actual = self.s.amountOfTime(root, 3)
        self.assertEqual(actual, 4)
        
    def test_case_2(self):
        root = deserialize("1")
        actual = self.s.amountOfTime(root, 1)
        self.assertEqual(actual, 0)

    def test_case_3(self):
        root = deserialize("1,2,3")
        actual = self.s.amountOfTime(root, 1)
        self.assertEqual(actual, 1)

if __name__ == '__main__':
    unittest.main()

