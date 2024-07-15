import unittest
from typing import List


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        cache = {}

        def dp(sub: str):
            ans = 0
            if sub in cache:
                print("hit")
                return cache[sub]
            for i in range(len(sub) - 1):
                if sub[i] == 'a' and sub[i + 1] == 'b':
                    sub_ans = dp(sub[:i] + sub[i + 2:]) + x
                    ans = max(ans, sub_ans)
                elif sub[i] == 'b' and sub[i + 1] == 'a':
                    sub_ans = dp(sub[:i] + sub[i + 2:]) + y
                    ans = max(ans, sub_ans)
            cache[sub] = ans
            return ans

        return dp(s)


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.maximumGain(s="cdbcbbaaabab", x=4, y=5)
        self.assertEqual(actual, 19)

    def test_case_2(self):
        actual = self.s.maximumGain(s="aabbaaxybbaabb", x=5, y=4)
        self.assertEqual(actual, 20)

    def test_case_3(self):
        actual = self.s.maximumGain(s="abcde", x=5, y=4)
        self.assertEqual(actual, 5)

    def test_case_4(self):
        actual = self.s.maximumGain(s="abcdeeeeabeeeeba", x=5, y=4)
        self.assertEqual(actual, 14)

    # def test_case_5(self):
    #     actual = self.s.maximumGain(s="aabbrtababbabmaaaeaabeawmvaataabnaabbaaaybbbaabbabbbjpjaabbtabbxaaavsmmnblbbabaeuasvababjbbabbabbasxbbtgbrbbajeabbbfbarbagha", x=8484, y=4096)
    #     self.assertEqual(actual, 14)

if __name__ == '__main__':
    unittest.main()
