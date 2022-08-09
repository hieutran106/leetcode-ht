from typing import List

'''
Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 

Return the number of negative numbers in grid.
'''
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            for v in row[::-1]:
                if v >=0:
                    break
                count += 1

        return count


