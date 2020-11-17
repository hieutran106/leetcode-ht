import unittest
from .solution import Solution
from .solution2 import Solution2

class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        s = Solution2()
        actual = s.countBits(2)
        self.assertEqual( [0,1,1], actual)

    def test_case_2(self):
        s = Solution2()
        actual = s.countBits(5)
        self.assertEqual(actual, [0,1,1,2,1,2])

    def test_case_3(self):
        s = Solution2()
        actual = s.countBits(0)
        self.assertEqual(actual, [0])

    def test_case_4(self):
        s = Solution2()
        actual = s.countBits(1)
        self.assertEqual(actual, [0, 1])

    def test_case_5(self):
        s = Solution2()
        actual = s.countBits(8)
        self.assertEqual(actual, [0, 1, 1, 2, 1, 2, 2, 3, 1])

if __name__ == '__main__':
    unittest.main()
