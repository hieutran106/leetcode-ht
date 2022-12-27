import unittest
from .solution import Solution
from utils.my_tree import deserialize

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        root = deserialize("1,2,3")
        actual = self.s.maxPathSum(root)
        self.assertEqual(6, actual)

    def test_case_2(self):
        root = deserialize("-10,9,20,null,null,15,7")
        actual = self.s.maxPathSum(root)
        self.assertEqual(42, actual)

    def test_case_3(self):
        root = deserialize("1")
        actual = self.s.maxPathSum(root)
        self.assertEqual(1, actual)

    def test_case_4(self):
        root = deserialize("")
        actual = self.s.maxPathSum(root)
        self.assertEqual(0, actual)

    def test_case_5(self):
        root = deserialize("-1,2,3")
        actual = self.s.maxPathSum(root)
        self.assertEqual(4, actual)

    def test_case_6(self):
        root = deserialize("-1,-2,3")
        actual = self.s.maxPathSum(root)
        self.assertEqual(3, actual)

    def test_case_7(self):
        root = deserialize("-2,-1")
        actual = self.s.maxPathSum(root)
        self.assertEqual(-1, actual)

    def test_case_8(self):
        root = deserialize("2,-1")
        actual = self.s.maxPathSum(root)
        self.assertEqual(2, actual)

    def test_case_9(self):
        root = deserialize("1,-2,-3,1,3,-2,null,-1")
        actual = self.s.maxPathSum(root)
        self.assertEqual(3, actual)

    def test_case_10(self):
        root = deserialize("-1,null,9,-6,3,null,null,null,-2")
        actual = self.s.maxPathSum(root)
        self.assertEqual(12, actual)

if __name__ == '__main__':
    unittest.main()

