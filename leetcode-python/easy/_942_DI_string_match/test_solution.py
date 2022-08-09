import unittest
from .solution import Solution


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        actual = s.diStringMatch("IDID")
        self.assertEqual(actual, [0, 4, 1, 3, 2])


    def test_case2(self):
        s = Solution()
        actual = s.diStringMatch("III")
        self.assertEqual(actual, [0, 1, 2, 3])

    def test_case3(self):
        s = Solution()
        actual = s.diStringMatch("DDI")
        self.assertEqual(actual, [3, 2, 0, 1])

    def test_case4(self):
        s = Solution()
        actual = s.diStringMatch("DDD")
        self.assertEqual(actual, [3, 2, 1, 0])

    def test_case5(self):
        s = Solution()
        actual = s.diStringMatch("IDDI")
        self.assertEqual(actual, [0, 4, 3, 1, 2])

    def test_case6(self):
        s = Solution()
        actual = s.diStringMatch("IDDI")
        self.assertCountEqual(actual, [2, 4, 3, 0, 1])

if __name__ == '__main__':
    unittest.main()
