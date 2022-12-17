from typing import List

def max_from_side(height: List[int], side = 'left'):
    n = len(height)
    max_array = [0 for _ in range(n)]
    curr_max = 0
    # default, scan from left -> right to find max from the left
    enumerable = enumerate(height)
    if side == 'right':
        enumerable = reversed(list(enumerable))
    for i, val in enumerable:
        max_array[i] = curr_max
        if height[i] > curr_max:
            curr_max = height[i]
    return max_array


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = 0
        # calculate max_left
        max_left = max_from_side(height, 'left')
        # calculate max_right
        max_right = max_from_side(height, 'right')
        # calculate water
        for i, val in enumerate(height):
            acc = min(max_left[i], max_right[i]) - height[i]
            water += max(acc, 0)
        return water



