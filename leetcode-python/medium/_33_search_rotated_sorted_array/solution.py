from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m_index = (l + r) // 2
            m = nums[m_index]
            if m == target:
                return m_index
            if nums[l] <= m:
                # we have left sorted half
                if target < nums[l] or target > m:
                    # search in right part
                    l = m_index + 1
                else:
                    # search in left part
                    r = m_index - 1
            else:
                # we have right sorted half
                if target < m or target > nums[r]:
                    r = m_index -1
                else:
                    l = m_index + 1
        return -1
