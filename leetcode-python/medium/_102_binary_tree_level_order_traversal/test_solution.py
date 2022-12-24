import unittest
from .solution import Solution
from utils.my_tree import deserialize

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        root = deserialize("3,9,20,null,null,15,7")
        actual = self.s.levelOrder(root)
        self.assertEqual([[3],[9,20],[15,7]], actual)

    def test_case_2(self):
        root = deserialize("1")
        actual = self.s.levelOrder(root)
        self.assertEqual([[1]], actual)

    def test_case_3(self):
        root = deserialize("")
        actual = self.s.levelOrder(root)
        self.assertEqual([], actual)

    def test_case_4(self):
        root = deserialize("1,2,3,4,5,null,6,7,null,8")
        actual = self.s.levelOrder(root)
        self.assertEqual([[1],[2,3],[4,5,6],[7,8]], actual)

if __name__ == '__main__':
    unittest.main()

