import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        actual = self.s.frequencySort("tree")
        self.assertEqual(actual, "eetr")

    def test_case2(self):
        actual = self.s.frequencySort("cccaaa")
        self.assertEqual("cccaaa", actual)

    def test_case3(self):
        actual = self.s.frequencySort("Aabb")
        self.assertEqual("bbAa", actual)

    def test_case4(self):
        actual = self.s.frequencySort("loveleetcode")
        self.assertEqual("eeeelloovtcd", actual)


if __name__ == '__main__':
    unittest.main()

