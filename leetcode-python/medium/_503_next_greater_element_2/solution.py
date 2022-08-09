from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        double = nums + nums
        # use decreasing stack
        result = [-1] * len(double)
        stack = []
        for i in range(len(double)):
            while stack and double[i] > double[stack[-1]]:
                top = stack.pop()
                result[top] = double[i]

            stack.append(i)

        # take half of the double
        result = result[:len(result)//2]
        return result
