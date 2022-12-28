import unittest
from .solution import Solution
from utils.my_tree import deserialize

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        root = deserialize("1,2,3,null,5,null,4")
        actual = self.s.rightSideView(root)
        self.assertEqual([1,3,4], actual)

    def test_case_2(self):
        root = deserialize("1,null,3")
        actual = self.s.rightSideView(root)
        self.assertEqual([1,3], actual)

    def test_case_3(self):
        root = None
        actual = self.s.rightSideView(root)
        self.assertEqual([], actual)

if __name__ == '__main__':
    unittest.main()

