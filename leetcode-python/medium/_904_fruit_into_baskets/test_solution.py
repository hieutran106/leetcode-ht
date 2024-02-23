import collections
import unittest
from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # If the current window is valid - i.e. if it contains at most 2 distinct fruits - we expand the window to include the next fruit
        # If the current window is not valid, we contract the window by repeatedly removing the leftmost fruit
        n = len(fruits)
        l = 0
        r =0
        counter = collections.defaultdict(int)
        max_fruit = float("-inf")
        while r < n:
            # expand
            counter[fruits[r]] += 1
            r += 1
            while len(counter.keys()) > 2:
                counter[fruits[l]] -= 1
                if counter[fruits[l]] == 0:
                    del counter[fruits[l]]
                l += 1
            max_fruit = max(max_fruit, r - l)

        return max_fruit
class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.totalFruit(fruits = [1,2,1])
        self.assertEqual(3, actual)
        
    def test_case_2(self):
        actual = self.s.totalFruit(fruits = [0,1,2,2])
        self.assertEqual(3, actual)

    def test_case_3(self):
        actual = self.s.totalFruit(fruits = [1,2,3,2,2])
        self.assertEqual(4, actual)

    def test_case_4(self):
        actual = self.s.totalFruit(fruits = [1,1,2,2,3,3,4,4,4,4,5])
        self.assertEqual(6, actual)

    def test_case_5(self):
        actual = self.s.totalFruit(fruits = [1,1,2,3,2,3,4])
        self.assertEqual(4, actual)

if __name__ == '__main__':
    unittest.main()

