import unittest
from typing import List


class Solution:

    def maximumSwap(self, num: int) -> int:
        """
        Suffix max right
        For each index, what is the bigger number on the right
        """
        def evaluate(nums):
            ans = 0
            for n in nums:
                ans = ans*10 + n
            return ans
        ans = num
        nums = []
        for c in str(num):
            nums.append(int(c))
        max_right = nums[-1]
        max_index = len(nums) - 1
        for i in range(len(nums) -2, -1, -1):
            if nums[i] < max_right:
                # possible candidate
                nums[i], nums[max_index] = nums[max_index], nums[i]
                print(f"Candidate {evaluate(nums)}")
                ans = max(ans, evaluate(nums))
                nums[i], nums[max_index] = nums[max_index], nums[i]
            elif nums[i] > max_right:
                max_right = nums[i]
                max_index = i
        return ans


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.maximumSwap(num=2736)
        self.assertEqual(7236, actual)

    def test_case_2(self):
        actual = self.s.maximumSwap(num=9973)
        self.assertEqual(9973, actual)

    def test_case_3(self):
        actual = self.s.maximumSwap(num=1250)
        self.assertEqual(5210, actual)

    def test_case_4(self):
        actual = self.s.maximumSwap(num=886723)
        self.assertEqual(887623, actual)

    def test_case_5(self):
        actual = self.s.maximumSwap(num=882167)
        self.assertEqual(887162, actual)

    def test_case_6(self):
        actual = self.s.maximumSwap(num=88123456)
        self.assertEqual(88623451, actual)

    def test_case_7(self):
        actual = self.s.maximumSwap(num=0)
        self.assertEqual(0, actual)

    def test_case_8(self):
        actual = self.s.maximumSwap(num=1993)
        self.assertEqual(9913, actual)


if __name__ == '__main__':
    unittest.main()
