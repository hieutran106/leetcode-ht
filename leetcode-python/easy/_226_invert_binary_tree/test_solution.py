import unittest
from .solution import Solution
from utils.my_tree import deserialize, serialize


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def testCase1(self):
        root = deserialize("2,1,3")
        invert = self.s.invertTree(root)
        expect = serialize(invert)
        self.assertEqual(expect, "2,3,1")

    def testCase2(self):
        root = deserialize("")
        invert = self.s.invertTree(root)
        expect = serialize(invert)
        self.assertEqual(expect, "")

    def testCase3(self):
        root = deserialize("4,2,7,1,3,6,9")
        invert = self.s.invertTree(root)
        expect = serialize(invert)
        self.assertEqual(expect, "4,7,2,9,6,3,1")

if __name__ == '__main__':
    unittest.main()

