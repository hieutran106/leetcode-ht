import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        actual = self.s.sumSubarrayMins([3, 1, 2, 4])
        self.assertEqual(17, actual)

if __name__ == '__main__':
    unittest.main()

