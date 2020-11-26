import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        actual = self.s.shortestToChar("loveleetcode", "e")
        self.assertEqual(actual, [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0])

if __name__ == '__main__':
    unittest.main()

