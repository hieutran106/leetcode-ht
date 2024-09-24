import unittest
from typing import List
import utils.my_tree
import utils.my_list
class Solution:
    def isSubPath(self, head, root) -> bool:
        return False
class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        root =  utils.my_tree.deserialize("1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3")
        head = utils.my_list.deserialize("4,2,8")
        actual = self.s.isSubPath(head, root)
        self.assertEqual(True, actual)
        
    def test_case_2(self):
        root = utils.my_tree.deserialize("1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3")
        head = utils.my_list.deserialize("1,4,2,6")
        actual = self.s.isSubPath(head, root)
        self.assertEqual(True, actual)

    def test_case_3(self):
        root = utils.my_tree.deserialize("1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3")
        head = utils.my_list.deserialize("1,4,2,6,8")
        actual = self.s.isSubPath(head, root)
        self.assertEqual(False, actual)

    def test_case_4(self):
        root = utils.my_tree.deserialize("1")
        head = utils.my_list.deserialize("1")
        actual = self.s.isSubPath(head, root)
        self.assertEqual(True, actual)

if __name__ == '__main__':
    unittest.main()

