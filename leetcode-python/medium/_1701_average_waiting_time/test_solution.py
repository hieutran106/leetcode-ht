import unittest
from typing import List
import collections

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:

        ans = 0
        finish_time = 0
        for arrive_time, prepare_time in customers:
            start_to_cook = arrive_time if arrive_time > finish_time else finish_time
            finish_time = start_to_cook + prepare_time
            ans += finish_time - arrive_time
            print(f"Customer wait for {finish_time - arrive_time}")

        return ans / len(customers)

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.averageWaitingTime(customers = [[1,2],[2,5],[4,3]])
        self.assertEqual(actual, 5.0)
        
    def test_case_2(self):
        actual = self.s.averageWaitingTime(customers=[[5,2],[5,4],[10,3],[20,1]])
        self.assertEqual(actual, 3.25)

if __name__ == '__main__':
    unittest.main()

