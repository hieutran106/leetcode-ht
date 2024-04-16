import collections
import unittest
from typing import List
from utils.my_list import deserialize

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixSum = 0
        # use a dict to store previous range sum {rangeSum: occurrence}
        history = collections.defaultdict(int)
        history[0] = 1
        res = 0
        for n in nums:
            prefixSum += n
            if prefixSum - goal in history:
                res += history[prefixSum - goal]
            # store frequency
            history[prefixSum] += 1
        return res


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.numSubarraysWithSum(nums=[1, 0, 1, 0, 1], goal=2)
        self.assertEqual(actual, 4)

    def test_case_2(self):
        actual = self.s.numSubarraysWithSum(nums=[0, 0], goal=0)
        self.assertEqual(actual, 3)

        actual = self.s.numSubarraysWithSum(nums=[0, 0, 0, 0, 0], goal=0)
        self.assertEqual(actual, 15)

    def test_case_4(self):
        actual = self.s.numSubarraysWithSum(nums=[1, 1, 1, 1], goal=4)
        self.assertEqual(actual, 1)

    def test_case_5(self):
        actual = self.s.numSubarraysWithSum(nums=[1, 1, 1, 1], goal=0)
        self.assertEqual(actual, 0)

    def test_case_6(self):
        actual = self.s.numSubarraysWithSum(nums=[1, 1, 0, 1], goal=0)
        self.assertEqual(actual, 1)

    def test_case_7(self):
        actual = self.s.numSubarraysWithSum(nums=[0, 0, 1, 1, 0, 0], goal=2)
        self.assertEqual(actual, 9)

    def test_case_8(self):
        actual = self.s.numSubarraysWithSum(nums=[0, 0, 0, 0], goal=0)
        self.assertEqual(actual, 10)

    def test_case_3(self):
        return
        with open('test3_input.txt') as f:
            # Read the contents of the file into a variable
            data = f.read()
            nums = deserialize(data)
            actual = self.s.numSubarraysWithSum(nums, goal=1159)
            self.assertEqual(actual, 186702)


if __name__ == '__main__':
    unittest.main()

