from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [nums[0]]
        for i in range(1, n):
            prefix_sum.append(nums[i] + prefix_sum[-1])

        total = 0
        d = {0: 1}
        for sum_value in prefix_sum:
            # See if we see (sum - k) before or not
            # it means that sum[j] - sum[i] == k, i < j
            # thus, we found a subarray whose sum is equal to k
            key = sum_value - k
            if key in d:
                total = total + d[key]

            if sum_value in d:
                d[sum_value] += 1
            else:
                d[sum_value] = 1

        return total
