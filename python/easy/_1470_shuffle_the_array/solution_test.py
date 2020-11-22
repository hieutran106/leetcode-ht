import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()


    def test_case1(self):
        actual = self.s.shuffle([2,5,1,3,4,7], 3)
        self.assertEqual([2,3,5,4,1,7], actual)

    def test_case2(self):
        actual = self.s.shuffle([1,2,3,4,4,3,2,1], 4)
        self.assertEqual([1,4,2,3,3,2,4,1], actual)

    def test_case3(self):
        actual = self.s.shuffle([1,1,2,2], 2)
        self.assertEqual([1,2,1,2], actual)


if __name__ == '__main__':
    unittest.main()
