import unittest
from typing import List, Optional
from utils.my_tree import TreeNode, deserialize
import collections

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = collections.deque([root])
        curr_index = 0
        while q:
            n = len(q)
            tmp = []
            for i in range(n):
                node = q.popleft()
                tmp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # check value
            for value in tmp:
                if (value + curr_index) % 2 == 0:
                    return False
            # check order
            for i in range(1, len(tmp)):
                if curr_index % 2 == 0: # even -> increasing
                    if tmp[i] <= tmp[i-1]:
                        return False
                else: # odd -> should be decreasing
                    if tmp[i] >= tmp[i-1]:
                        return False
            curr_index += 1
        return True





class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        root = deserialize("1,10,4,3,null,7,9,12,8,6,null,null,2")
        actual = self.s.isEvenOddTree(root)
        self.assertEqual(True, actual)

    def test_case_2(self):
        root = deserialize("5,4,2,3,3,7")
        actual = self.s.isEvenOddTree(root)
        self.assertEqual(False, actual)

    def test_case_3(self):
        root = deserialize("5,9,1,3,5,7")
        actual = self.s.isEvenOddTree(root)
        self.assertEqual(False, actual)

    def test_case_4(self):
        root = deserialize("15,184,180,25,29,33,37,126,122,118,114,112,108,106,104,27,29,33,35,37,41,43,null,null,null,null,null,47,49,53,57,null,null,168,null,164,162,158,null,156,null,152,98,null,null,96,92,90,null,88,86,84,null,89,null,91,null,null,null,95,99,null,null,null,null,null,null,101,105,107,111,null,null,null,null,null,null,null,null,null,null,null,null,118,null,114,null,112,110,108,104,100,96,94,null,99,null,103,null,105,107,111,null,null,null,115,null,119,null,91,null,null,null,128,null,124,120,118,null,114,null,null,null,null,null,null,null,null,null,75,null,79,null,81,null,null,null,null,null,null,null,null,null,182,null,61")
        actual = self.s.isEvenOddTree(root)
        self.assertEqual(False, actual)

    def test_case_5(self):
        root = deserialize("1")
        actual = self.s.isEvenOddTree(root)
        self.assertEqual(True, actual)

    def test_case_6(self):
        root = deserialize("2")
        actual = self.s.isEvenOddTree(root)
        self.assertEqual(False, actual)

    def test_case_6(self):
        root = deserialize("1,10,4,3,null,7,9,12,8,10,null,null,2")
        actual = self.s.isEvenOddTree(root)
        self.assertEqual(False, actual)

    def test_case_7(self):
        root = deserialize("1,10,4,7,null,7,9,12,8,6,null,null,2")
        actual = self.s.isEvenOddTree(root)
        self.assertEqual(False, actual)


if __name__ == '__main__':
    unittest.main()
