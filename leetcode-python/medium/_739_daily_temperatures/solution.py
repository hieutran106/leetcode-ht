from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Use a stack to store (index, value)
        The values in stack is in decreasing order
        :param temperatures:
        :return:
        """
        result = [0] * len(temperatures)
        stack = []
        for i, value in enumerate(temperatures):
            while len(stack) > 0 and value > stack[-1][1]:
                item = stack.pop()
                result[item[0]] = i - item[0]
            stack.append((i, value))
        return result
