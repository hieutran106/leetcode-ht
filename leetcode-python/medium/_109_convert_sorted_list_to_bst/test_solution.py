import unittest
from .solution import Solution
from utils.my_list import ListNode, createListFromArray
from utils.my_tree import TreeNode, serialize

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        head = createListFromArray([-10, -3, 0, 5, 9])
        root = self.s.sortedListToBST(head)
        serialized_tree = serialize(root)
        self.assertEqual(serialized_tree, '0,-3,9,-10,null,5')

    def test_case2(self):
        head = createListFromArray([1, 2, 3])
        root = self.s.sortedListToBST(head)
        serialized_tree = serialize(root)
        self.assertEqual(serialized_tree, '2,1,3')

    def test_case3(self):
        head = createListFromArray([])
        root = self.s.sortedListToBST(head)
        serialized_tree = serialize(root)
        self.assertEqual(serialized_tree, '')

    def test_case4(self):
        head = createListFromArray([0])
        root = self.s.sortedListToBST(head)
        serialized_tree = serialize(root)
        self.assertEqual(serialized_tree, '0')

    def test_case5(self):
        head = createListFromArray([1,3])
        root = self.s.sortedListToBST(head)
        serialized_tree = serialize(root)
        self.assertEqual(serialized_tree, '3,1')




if __name__ == '__main__':
    unittest.main()

