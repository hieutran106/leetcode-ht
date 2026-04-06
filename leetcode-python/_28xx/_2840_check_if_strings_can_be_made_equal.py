import collections
import unittest
from typing import List

# Date: 2026-03-31
# Problem: 2840 check_if_strings_can_be_made_equal
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        s1_even, s1_odd = collections.defaultdict(int), collections.defaultdict(int)
        s2_even, s2_odd = collections.defaultdict(int), collections.defaultdict(int)
        for i, (c1, c2) in enumerate(zip(s1, s2)):
            if i % 2 ==0:
                s1_even[c1]+= 1
                s2_even[c2] += 1
            else:
                s1_odd[c1] += 1
                s2_odd[c2] += 1

        return s1_even == s2_even and s1_odd == s2_odd

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.checkStrings(s1 = "abcdba", s2 = "cabdab")
        self.assertEqual(actual,True)
        
    def test_case_2(self):
        actual = self.s.checkStrings(s1 = "abe", s2 = "bea")
        self.assertEqual(actual, False)

if __name__ == '__main__':
    unittest.main()

