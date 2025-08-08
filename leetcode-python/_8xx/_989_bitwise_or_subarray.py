import unittest
from typing import List

# Date: 2025-08-08
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans = set()
        prev_or = set() # unique or value at previous index
        for n in arr:
            curr_or = {n}
            for e in prev_or:
                curr_or.add(e | n)
            ans.update(curr_or)
            prev_or = curr_or
        return len(ans)
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.subarrayBitwiseORs(arr = [0])
        self.assertEqual(1, actual)
        
    def test_case_2(self):
        actual = self.s.subarrayBitwiseORs(arr = [1,1,2])
        self.assertEqual(3, actual)

    def test_case_3(self):
        actual = self.s.subarrayBitwiseORs(arr = [1,2,4])
        self.assertEqual(6, actual)

if __name__ == '__main__':
    unittest.main()

