import unittest
from typing import List

# Date: 2026-04-13
# Problem: 1320 min_distance_to_type_a_word
class Solution:
    def minimumDistance(self, word: str) -> int:
        def get_distance(a, b):
            posA = ord(a) - ord('A')
            posB = ord(b) - ord('A')
            distance = abs(posA//6 - posB//6) + abs(posA%6 - posB % 6)
            return distance

        memo = {}
        def dp(i, j, k):
            # current char at i-th, while j,k for the two fingers
            if i == len(word):
                return 0
            if (i, j,k) in memo:
                return memo[(i, j, k)]
            # finger 1 selection
            if j != -1:
                s1 = get_distance(word[i], word[j]) if j != -1 else 0 + dp(i+1, i, k)
            else:
                s1 = dp(i+1, i, k)

            # finger 2 selection
            if k != -1:
                s2 = get_distance(word[i], word[k]) + dp(i+1, j, i)
            else:
                s2 = dp(i+1, j, i)
            res = min(s1, s2)
            memo[(i, j, k)] = res
            return res


        ans = dp(0, -1, -1)
        return ans
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.minimumDistance(word = "CAKE")
        self.assertEqual(3, actual)
        
    def test_case_2(self):
        actual = self.s.minimumDistance(word="HAPPY")
        self.assertEqual(6, actual)

    def test_case_3(self):
        actual = self.s.minimumDistance(word="CAXXXXXXXXXXX")
        self.assertEqual(2, actual)

if __name__ == '__main__':
    unittest.main()

