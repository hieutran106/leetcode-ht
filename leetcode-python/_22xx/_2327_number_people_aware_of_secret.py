import unittest
from typing import List

# Date: 2025-09-09
# Problem: 2327 number_people_aware_of_secret
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        # dp[i][j] - number of people know the secret at day i, forget = j
        MOD = 10 ** 9 + 7
        dp = [[0 for _ in range(forget + 1)] for _ in range(n+1)]
        dp[1][forget] = 1
        for i in range(2, n + 1):
            sharable = 0
            for j in range(1, forget):
                dp[i][j] = dp[i-1][j+1]
                if j <= forget - delay:
                    sharable = (sharable + dp[i-1][j+1]) % MOD

            dp[i][forget] = sharable
        ans = 0
        for j in range(1, forget + 1):
            ans = (ans + dp[n][j]) % MOD
        return ans
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.peopleAwareOfSecret(n = 6, delay = 2, forget = 4)
        self.assertEqual(5, actual)
        
    def test_case_2(self):
        actual = self.s.peopleAwareOfSecret(n = 4, delay = 1, forget = 3)
        self.assertEqual(6, actual)

    def test_case_3(self):
        actual = self.s.peopleAwareOfSecret(n = 2, delay = 1, forget = 2)
        self.assertEqual(2, actual)

    def test_case_4(self):
        actual = self.s.peopleAwareOfSecret(n = 50, delay = 5, forget = 8)
        self.assertEqual(6757, actual)


if __name__ == '__main__':
    unittest.main()

