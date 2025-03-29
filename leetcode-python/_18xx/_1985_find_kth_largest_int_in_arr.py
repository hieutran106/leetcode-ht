import unittest
from typing import List
import functools

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        def compare(a: str, b: str):
            if len(a) < len(b):
                return -1
            elif len(a) > len(b):
                return 1
            else:
                for i in range(len(a)):
                    if a[i] < b[i]:
                        return -1
                    elif a[i] > b[i]:
                        return 1
                return 0
        key = functools.cmp_to_key(compare)
        nums.sort(key=key)
        print(nums)
        return nums[len(nums) - k]


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.kthLargestNumber(nums=["3", "6", "7", "10"], k=4)
        self.assertEqual(actual, "3")

    def test_case_2(self):
        actual = self.s.kthLargestNumber(nums=["2", "21", "12", "1"], k=3)
        self.assertEqual(actual, "2")

    def test_case_3(self):
        actual = self.s.kthLargestNumber(nums=["0", "0"], k=2)
        self.assertEqual(actual, "0")


if __name__ == '__main__':
    unittest.main()
