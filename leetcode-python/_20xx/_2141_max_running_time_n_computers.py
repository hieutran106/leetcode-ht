import unittest
from typing import List

# Date: 2025-12-01
# Problem: 2141 max_running_time_n_computers
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def good(minute: int) ->bool:
            total = 0
            for b in batteries:
                total += min(minute, b)
            return total >= minute * n
        l = 1
        r = sum(batteries) // n
        while l <= r:
            mid = (r + l) // 2
            if good(mid):
                l = mid + 1
            else:
                r = mid - 1
        return l - 1
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.maxRunTime(n = 2, batteries = [3,3,3])
        self.assertEqual(4, actual)
        
    def test_case_2(self):
        actual = self.s.maxRunTime(n = 2, batteries = [1,1,1,1])
        self.assertEqual(2, actual)

    def test_case_3(self):
        actual = self.s.maxRunTime(n = 2, batteries = [3, 4, 5])
        self.assertEqual(6, actual)

    def test_case_6(self):
        actual = self.s.maxRunTime(n = 3, batteries = [10,10,3,5])
        self.assertEqual(8, actual)

if __name__ == '__main__':
    unittest.main()

