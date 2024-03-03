import collections
import unittest

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        c = collections.Counter(s)
        return (c['1'] - 1) * '1' + c['0']*'0' + '1'
class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.maximumOddBinaryNumber("010")
        self.assertEqual("001", actual)
        
    def test_case_2(self):
        actual = self.s.maximumOddBinaryNumber("0101")
        self.assertEqual("1001", actual)

    def test_case_3(self):
        actual = self.s.maximumOddBinaryNumber("0111")
        self.assertEqual("1101", actual)

    def test_case_4(self):
        actual = self.s.maximumOddBinaryNumber("111")
        self.assertEqual("111", actual)

    def test_case_5(self):
        actual = self.s.maximumOddBinaryNumber("10111")
        self.assertEqual("11101", actual)



if __name__ == '__main__':
    unittest.main()

