import unittest
from typing import List, Optional
from utils.my_tree import TreeNode, serialize
import collections

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        mapper = collections.defaultdict(lambda val: TreeNode(val))
        all_nodes = set()
        children = set()
        for parent, child, is_left in descriptions:
            parent_node = mapper[parent]
            parent_node.val = parent
            child_node = mapper[child]
            child_node.val = child
            if is_left:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
            all_nodes.add(parent)
            all_nodes.add(child)
            children.add(child)
        root = list(all_nodes - children)[0]
        return mapper[root]


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.createBinaryTree(descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]])
        serialized_root = serialize(actual)
        self.assertEqual(serialized_root, "50,20,80,15,17,19")
        
    def test_case_2(self):
        actual = self.s.createBinaryTree(descriptions=[[1,2,1],[2,3,0],[3,4,1]])
        serialized_root = serialize(actual)
        self.assertEqual(serialized_root, "1,2,null,null,3,4")

if __name__ == '__main__':
    unittest.main()

