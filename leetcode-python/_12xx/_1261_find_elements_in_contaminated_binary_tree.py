import unittest
from typing import List, Optional
from utils.my_tree import TreeNode, deserialize


class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        visit = set()

        def fix(node: TreeNode, val: int):
            if node is None:
                return
            node.val = val
            visit.add(val)
            if node.left:
                fix(node.left, 2 * val + 1)
            if node.right:
                fix(node.right, 2 * val + 2)

        fix(root, 0)
        self.visit = visit

    def find(self, target: int) -> bool:
        return target in self.visit


class MyTestCase(unittest.TestCase):

    def test_case_1(self):
        root = deserialize("-1,null,-1")
        find = FindElements(root)
        self.assertEqual(False, find.find(1))
        self.assertEqual(True, find.find(2))

    def test_case_2(self):
        root = deserialize("-1,-1,-1,-1,-1")
        find = FindElements(root)
        self.assertEqual(True, find.find(1))
        self.assertEqual(True, find.find(3))
        self.assertEqual(False, find.find(5))

    def test_case_3(self):
        root = deserialize("-1,null,-1,-1,null,-1")
        find = FindElements(root)
        self.assertEqual(True, find.find(2))
        self.assertEqual(False, find.find(3))
        self.assertEqual(False, find.find(4))
        self.assertEqual(True, find.find(5))


if __name__ == '__main__':
    unittest.main()
