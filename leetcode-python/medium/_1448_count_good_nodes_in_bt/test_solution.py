import unittest
from .solution import Solution
from utils.my_tree import deserialize

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        root = deserialize("3,1,4,3,null,1,5")
        actual = self.s.goodNodes(root)
        self.assertEqual(4, actual)

    def test_case_2(self):
        root = deserialize("3,3,null,4,2")
        actual = self.s.goodNodes(root)
        self.assertEqual(3, actual)

    def test_case_3(self):
        root = deserialize("1")
        actual = self.s.goodNodes(root)
        self.assertEqual(1, actual)

if __name__ == '__main__':
    unittest.main()

