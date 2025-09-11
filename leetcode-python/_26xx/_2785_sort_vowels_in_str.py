import unittest
from typing import List

# Date: 2025-11-09
# Problem: 2785 sort_vowels_in_str
class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []
        for c in s:
            if c.lower() in 'aeiou':
                vowels.append(c)
        vowels.sort()
        print(vowels)
        ans = []
        j = 0
        for c in s:
            if c.lower() in 'aeiou':
                ans.append(vowels[j])
                j+= 1
                continue
            ans.append(c)
        return "".join(ans)
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.sortVowels(s = "lEetcOde")
        self.assertEqual("lEOtcede", actual)
        
    def test_case_2(self):
        actual = self.s.sortVowels(s="lYmpH")
        self.assertEqual("lYmpH", actual)

    def test_case_3(self):
        actual = self.s.sortVowels(s="e")
        self.assertEqual("e", actual)

if __name__ == '__main__':
    unittest.main()

