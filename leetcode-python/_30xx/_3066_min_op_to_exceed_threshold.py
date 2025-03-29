import unittest
from typing import List
import heapq


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        heapq.heapify(nums)
        print(nums)
        while len(nums) >= 2 and nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums, min(x, y) * 2 + max(x, y))
            ans += 1
            print(f"After {ans} op, the nums is {nums}")

        return ans


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.minOperations(nums=[2, 11, 10, 1, 3], k=10)
        self.assertEqual(actual, 2)

    def test_case_2(self):
        actual = self.s.minOperations(nums=[1, 1, 2, 4, 9], k=20)
        self.assertEqual(actual, 4)


if __name__ == '__main__':
    unittest.main()
