from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the input array to eliminate duplicate answer
        nums = sorted(nums)
        n = len(nums)
        result = []
        for i in range(n -2):
            if i >= 1 and nums[i-1] == nums[i]:
                # already compute in earlier iteration
                continue
            target = - nums[i]
            left = i + 1
            right = n - 1
            while left < right:
                if left > i + 1 and nums[left] == nums[left - 1]:
                    left += 1
                    continue
                two_sum = nums[left] + nums[right]
                if two_sum == target:
                    ans = [nums[i], nums[left], nums[right]]
                    print(f"Found answer, {ans=}")
                    result.append(ans)
                    left += 1
                    right -= 1
                elif two_sum < target:
                    left += 1
                else:
                    right -= 1
        return result
