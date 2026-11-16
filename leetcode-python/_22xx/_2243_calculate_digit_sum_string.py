import unittest
from typing import List

# Date: 2026-11-16
# Problem: 2243 calculate_digit_sum_string
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            chunks = [s[i: i+k] for i in range(0, len(s), k)]
            round = []
            for chunk in chunks:
                digit_sum = sum([int(e) for e in chunk])
                round.append(digit_sum)
            s = "".join(str(n) for n in round)
        return s
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.digitSum(s = "11111222223", k = 3)
        self.assertEqual("135", actual)
        
    def test_case_2(self):
        actual = self.s.digitSum(s = "00000000", k = 3)
        self.assertEqual("000", actual)

if __name__ == '__main__':
    unittest.main()

