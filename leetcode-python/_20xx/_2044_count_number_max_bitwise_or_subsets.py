import unittest
from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # The maximum bitwise-OR is the bitwise-OR of the whole array.
        max_or = 0
        for n in nums:
            max_or = max_or | n
        print(f"{max_or=}")
        self.ans = 0

        def backtrack(i: int, curr_or: int, subset):
            if curr_or == max_or:
                print(f"Found subset {subset=}")
                self.ans += 1
            for j in range(i, len(nums)):
                subset.append(nums[j])
                backtrack(j + 1, curr_or | nums[j], subset)
                subset.pop()
        backtrack(0, 0, [])
        return self.ans


class Solution2:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        # Use dp to find max or value
        memo_max = {}
        def find_max(index: int, curr_or: int):
            if index == n:
                return curr_or
            if (index, curr_or) in memo_max:
                return memo_max[(index, curr_or)]
            res = max(
                find_max(index +1, curr_or | nums[index]),
                find_max(index + 1, curr_or)
            )
            memo_max[(index, curr_or)] = res
            return res
        max_or = find_max(0, 0)
        print(f"{max_or=}")

        # use another dp to find the count
        memo_count = {}
        def count_max(index, curr_or):
            if index == n:
                if curr_or == max_or:
                    return 1
                return 0
            # include current number
            if (index, curr_or) in memo_count:
                return memo_count[(index, curr_or)]
            count_with = count_max(index + 1, curr_or | nums[index])
            count_without = count_max(index +1, curr_or)
            res = count_with + count_without
            memo_count[(index, curr_or)] = res
            return res
        ans = count_max(0, 0)
        return ans

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution2()

    def test_case_1(self):
        actual = self.s.countMaxOrSubsets(nums=[3, 1])
        self.assertEqual(2, actual)

    def test_case_2(self):
        actual = self.s.countMaxOrSubsets(nums=[2, 2, 2])
        self.assertEqual(7, actual)

    def test_case_3(self):
        actual = self.s.countMaxOrSubsets(nums=[3, 2, 1, 5])
        self.assertEqual(6, actual)


if __name__ == '__main__':
    unittest.main()
