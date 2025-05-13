import unittest
from typing import List

# Date: 2025-14-05
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        counter = [0] * 26;
        for c in s:
            counter[ord(c) - ord('a')] += 1
        for _ in range(t):
            new_counter = [0] * 26
            # transform a -> y
            for i in range(25):
                new_counter[i+1] = counter[i]
            # transform z
            new_counter[0] = counter[25]
            new_counter[1] = new_counter[1] + counter[25]
            counter = new_counter
        ans = 0
        for i in range(26):
            ans = (ans + counter[i]) % (10**9 + 7)
        return ans

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.lengthAfterTransformations( s = "abcyy", t = 2)
        self.assertEqual(7, actual)
        
    def test_case_2(self):
        actual = self.s.lengthAfterTransformations(s = "azbk", t = 1)
        self.assertEqual(5, actual)

    def test_case_3(self):
        actual = self.s.lengthAfterTransformations(s = "abcz", t = 2)
        self.assertEqual(5, actual)

if __name__ == '__main__':
    unittest.main()

