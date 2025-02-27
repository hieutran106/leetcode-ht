import unittest
from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        l = len(nums[0])
        visit = set(nums)
        for i in range(2 ** l):
            binary = bin(i)[2:]
            binary = "0" * (l - len(binary)) + binary
            if binary not in visit:
                return binary
        return ""
class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.findDifferentBinaryString(nums = ["01","10"])
        self.assertIn(actual, ["11", "00"])
        
    def test_case_2(self):
        actual = self.s.findDifferentBinaryString(nums=["00", "01"])
        self.assertIn(actual, ["11", "10"])

    def test_case_3(self):
        actual = self.s.findDifferentBinaryString(nums = ["111","011","001"])
        self.assertIn(actual, ["101", "000", "010", "100", "110"])

if __name__ == '__main__':
    unittest.main()

