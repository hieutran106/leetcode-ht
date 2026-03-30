import unittest
from typing import List

# Date: 2026-03-31
# Problem: 2840 check_if_strings_can_be_made_equal
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        s1_even, s1_odd = [], []
        s2_even, s2_odd = [], []
        for i, c in enumerate(s1):
            if i % 2 == 0:
                s1_even.append(c)
            else:
                s1_odd.append(c)

        for i, c in enumerate(s2):
            if i % 2 == 0:
                s2_even.append(c)
            else:
                s2_odd.append(c)
        s1_even.sort()
        s1_odd.sort()
        s2_even.sort()
        s2_odd.sort()

        for i in range(len(s1_even)):
            if s1_even[i] != s2_even[i]:
                return False

        for i in range(len(s1_odd)):
            if s1_odd[i] != s2_odd[i]:
                return False

        return True

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

