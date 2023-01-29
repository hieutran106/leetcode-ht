import unittest
from .solution import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.findJudge(n=2, trust=[[1, 2]])
        self.assertEqual(2, actual)

    def test_case_2(self):
        actual = self.s.findJudge(n=3, trust=[[1, 3], [2, 3]])
        self.assertEqual(3, actual)

    def test_case_3(self):
        actual = self.s.findJudge(n=3, trust=[[1, 3], [2, 3], [3, 1]])
        self.assertEqual(-1, actual)


if __name__ == '__main__':
    unittest.main()
