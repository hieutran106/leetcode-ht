import unittest
from typing import List

class Solution:
    def punishmentNumber(self, n: int) -> int:
        ans = 0
        for i in range(1, n + 1):
            if self.is_punishment_element(i):
                ans += i * i
        return ans

    def is_punishment_element(self, n):
        digits = [int(d) for d in str(n*n)]
        print(digits)

        def to_number(nums: List[int]):
            number = 0
            for d in nums:
                number = number * 10 + d
            return number

        def dp(i, total) -> bool:
            if total < 0:
                return False

            if i == len(digits) and total == 0:
                return True

            for j in range(i, len(digits)):
                sub_number = to_number(digits[i: j + 1])
                if sub_number == 29:
                    print("test")
                print(f"For {digits}, consider sub_number {sub_number}, total left : {total - sub_number}")
                if dp(j + 1, total - sub_number) is True:
                    return True
            return False

        return dp(0, n)



class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()


    def test_case_1(self):
        actual = self.s.punishmentNumber(n = 10)
        self.assertEqual(182, actual)


    def test_case_2(self):
        actual = self.s.punishmentNumber(n=37)
        self.assertEqual(1478, actual)


    def test_case_3(self):
        actual = self.s.punishmentNumber(n=1)
        self.assertEqual(1, actual)

    def test_case_4(self):
        actual = self.s.is_punishment_element(36)
        self.assertEqual(True, actual)


    def test_t2(self):
        actual = self.s.is_punishment_element(12)
        self.assertEqual(False, actual)

if __name__ == '__main__':
    unittest.main()

