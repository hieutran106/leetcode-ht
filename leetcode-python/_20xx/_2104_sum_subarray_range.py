import unittest
from typing import List

# Date: 2025-16-07
def count_min(nums: List[int]):
    l, r = [0] * len(nums), [0] * len(nums)
    for i in range(len(nums)):
        r[i] = len(nums) - i # r[i] distance between nums[i] and its next_less_element (NLE), including nums[i] and excluding NLE
        l[i] = i + 1 # l[i] distance between nums[i] and its prev_less_element (PLE), including nums[i] and excluding PLE

    stack = [] # using increasing stack
    for i, n in enumerate(nums):
        while stack and n < stack[-1][0]:
            item = stack.pop()
            # nums[i] is the next less element of top item
            r[item[1]] = i - item[1]
        if stack:
            # top is the prev less element of nums[i]
            l[i] = i - stack[-1][1]
        stack.append((n, i))

    ans = [] # ans[i] is the number of subarrays in which nums[i] is the minimum
    for i in range(len(nums)):
        ans.append(l[i] * r[i])
    return ans

def count_max(nums: List[int]):
    l, r = [0] * len(nums), [0] * len(nums)
    for i in range(len(nums)):
        r[i] = len(nums) - i  # r[i] distance between nums[i] and its next_greater_element (NPE), including nums[i] and excluding NPE
        l[i] = i + 1  # l[i] distance between nums[i] and its prev_greater_element (PPE), including nums[i] and excluding PPE
    stack = [] # using decreasing stack
    for i, n in enumerate(nums):
        while stack and n > stack[-1][0]:
            item = stack.pop()
            r[item[1]] = i - item[1]
        if stack:
            l[i] = i - stack[-1][1]
        stack.append((n, i))

    ans = []  # ans[i] is the number of subarrays in which nums[i] is the maximum
    for i in range(len(nums)):
        ans.append(l[i] * r[i])
    return ans

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        min = count_min(nums)
        max = count_max(nums)
        ans = 0
        for i in range(len(nums)):
            ans = ans + nums[i] * (max[i] - min[i])
        return ans

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_count_min1(self):
        actual = count_min([1, 2, 3])
        self.assertEqual([3, 2, 1], actual)

    def test_count_min2(self):
        actual = count_min([3, 7, 8, 4])
        self.assertEqual([4, 2, 1, 3], actual)

    def test_count_max1(self):
        actual = count_max([1, 2, 3])
        self.assertEqual([1, 2, 3], actual)

    def test_case_1(self):
        actual = self.s.subArrayRanges([1,2,3])
        self.assertEqual(4, actual)
        
    def test_case_2(self):
        actual = self.s.subArrayRanges([1, 2, 3])
        self.assertEqual(4, actual)

    def test_case_3(self):
        actual = self.s.subArrayRanges([4,-2,-3,4,1])
        self.assertEqual(59, actual)

if __name__ == '__main__':
    unittest.main()

