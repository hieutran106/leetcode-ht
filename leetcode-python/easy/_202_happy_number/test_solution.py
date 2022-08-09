import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self) -> None:
        self.s = Solution()
        self.assertEqual(self.s.isHappy(19), True)

    def test_case2(self) -> None:
        self.s = Solution()
        self.assertEqual(self.s.isHappy(21), False)

    def test_case3(self) -> None:
        self.s = Solution()
        self.assertEqual(self.s.isHappy(37), False)

if __name__ == '__main__':
    unittest.main()

