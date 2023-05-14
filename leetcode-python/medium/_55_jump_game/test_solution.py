import unittest
from typing import List
import heapq


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        min_heap = []
        for i, v in enumerate(nums):
            # pop
            while min_heap and min_heap[0] < i:
                heapq.heappop(min_heap)

            # check
            if i > 0 and len(min_heap) == 0:
                return False
            # add
            if v != 0:
                heapq.heappush(min_heap, i + v)
        return True








class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):

        actual = self.s.canJump(nums = [2,3,1,1,4])

        self.assertEqual(True, actual)

    def test_case_2(self):
        actual = self.s.canJump(nums = [3,2,1,0,4])
        self.assertEqual(False, actual)

    def test_case_3(self):
        actual = self.s.canJump(nums = [1])
        self.assertEqual(True, actual)

    def test_case_4(self):
        actual = self.s.canJump(nums = [1, 0])
        self.assertEqual(True, actual)

    def test_case_5(self):
        actual = self.s.canJump(nums = [0, 1])
        self.assertEqual(False, actual)

    def test_case_6(self):
        actual = self.s.canJump(nums=[0, 2, 3])
        self.assertEqual(False, actual)

    def test_case_7(self):
        actual = self.s.canJump(nums=[1, 2, 3])
        self.assertEqual(True, actual)

    def test_case_8(self):
        actual = self.s.canJump(nums=[0])
        self.assertEqual(True, actual)

    def test_case_9(self):
        actual = self.s.canJump(nums=[1, 2])
        self.assertEqual(True, actual)

if __name__ == '__main__':
    unittest.main()

