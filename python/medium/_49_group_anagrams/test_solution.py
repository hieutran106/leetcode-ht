import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        actual = self.s.groupAnagrams([""])
        self.assertEqual(actual, [[""]])

    def test_case2(self):
        actual = self.s.groupAnagrams(["a"])
        self.assertEqual(actual, [["a"]])

    def test_case3(self):
        actual = self.s.groupAnagrams( ["eat","tea","tan","ate","nat","bat"])
        self.assertEqual(len(actual), 3)

if __name__ == '__main__':
    unittest.main()

