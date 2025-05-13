import unittest
from typing import List
import collections
#2025-13-05
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        counter = collections.Counter(digits)
        ans = []
        for i in range(100, 1000, 2):
            a = i // 100
            b = (i - a * 100) // 10
            c = (i - a*100 -b * 10)
            req_b = 1 if a ==b else 0
            req_c = 0
            if a==c or b==c:
                req_c = 1
            if a==c and b==c:
                req_c = 2
            if counter[a] > 0 and counter[b] > req_b and counter[c] > req_c:
                ans.append(i)
        return ans
class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.findEvenNumbers(digits = [2,1,3,0])
        self.assertEqual(actual, [102,120,130,132,210,230,302,310,312,320])
        
    def test_case_2(self):
        actual = self.s.findEvenNumbers(digits = [2,2,8,8,2])
        self.assertEqual(actual, [222,228,282,288,822,828,882])

    def test_case_3(self):
        actual = self.s.findEvenNumbers(digits = [3,7,5])
        self.assertEqual(actual, [])

    def test_case_4(self):
        actual = self.s.findEvenNumbers(digits = [3, 1, 0])
        self.assertEqual(actual, [130, 310])

if __name__ == '__main__':
    unittest.main()

