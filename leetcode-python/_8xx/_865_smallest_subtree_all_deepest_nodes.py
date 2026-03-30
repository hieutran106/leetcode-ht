import unittest
from typing import List, Optional
from utils.my_tree import TreeNode, deserialize, serialize
import collections

# Date: 2026-01-15
# Problem: 865 smallest_subtree_all_deepest_nodes
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Step 1 - BFS to get the deepest node, during that get the link from child to parent
        q = collections.deque([root])
        deepest_nodes = []
        parent_map = {}
        while q:
            deepest_nodes = [n for n in q]
            for n in deepest_nodes:
                if n.left:
                    q.append(n.left)
                    parent_map[n.left] = n
                if n.right:
                    q.append(n.right)
                    parent_map[n.right] = n
                q.popleft()

        print([n.val for n in deepest_nodes])

        return None
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        root = deserialize("3,5,1,6,2,0,8,null,null,7,4")
        actual = self.s.subtreeWithAllDeepest(root)
        actual_str = serialize(actual)
        self.assertEqual("2,7,4", actual_str)
        
    def test_case_2(self):
        root = deserialize("0,1,3,null,2")
        actual = self.s.subtreeWithAllDeepest(root)
        actual_str = serialize(actual)
        self.assertEqual("2", actual_str)

    def test_case_3(self):
        root = deserialize("1")
        actual = self.s.subtreeWithAllDeepest(root)
        actual_str = serialize(actual)
        self.assertEqual("1", actual_str)

if __name__ == '__main__':
    unittest.main()

