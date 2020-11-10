class Solution:
    def maxPower(self, s: str) -> int:
        nums = []
        count = 1
        modified_s = s + 'A'
        for index, c in enumerate(modified_s):
            if index == len(modified_s) - 1: # reach pivot
                nums.append(count)
                break

            if c == modified_s[index- 1]:
                count += 1
            else:
                nums.append(count)
                count = 1

        return max(nums)
