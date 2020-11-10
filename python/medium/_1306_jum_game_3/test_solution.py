import unittest
from .solution import Solution


class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        s = Solution()
        actual = s.canReach([4, 2, 3, 0, 3, 1, 2], 5)
        self.assertEqual(actual, True)

        actual = s.canReach([4, 2, 3, 0, 3, 1, 2], 0)
        self.assertEqual(actual, True)

    def test_case_2(self):
        s = Solution()
        actual = s.canReach([3, 0, 2, 1, 2], 2)
        self.assertEqual(actual, False)


if __name__ == '__main__':
    unittest.main()
