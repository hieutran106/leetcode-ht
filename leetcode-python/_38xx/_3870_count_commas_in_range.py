import unittest
from typing import List

# Date: 2026-09-09
# Problem: 3870 count_commas_in_range
class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        return n - 1000 + 1
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.countCommas(n = 1002)
        self.assertEqual(3, actual)
        
    def test_case_2(self):
        actual = self.s.countCommas(n=998)
        self.assertEqual(0, actual)

if __name__ == '__main__':
    unittest.main()

