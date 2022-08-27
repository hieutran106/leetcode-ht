from typing import List
import re

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        memo = {}
        expr = re.split("([^0-9])", expression)
        def dp(expr: List[str], start: int, end: int) -> List[int]:
            if len(expr[start: end]) == 1:
                val = int(expr[start])
                return [val]
            if (start, end) in memo:
                return memo[(start, end)]
            result = []
            for i in range(start + 1, end, 2):
                # print(f"Evaluate left from: {start} to: {i}, expr={expr[start:i]}")
                # print(f"Evaluate right from: {i+1} to: {end}, expr={expr[i+1:end]}")
                left_values = dp(expr, start, i)
                right_values = dp(expr, i+1, end)
                op = expr[i]
                # print(f"Op:{op}")
                for l_val in left_values:
                    for r_val in right_values:
                        if op == '+':
                            result.append(l_val + r_val)
                        elif op == '-':
                            result.append(l_val - r_val)
                        else:
                            result.append(l_val * r_val)
            memo[(start, end)] = result
            return result

        return dp(expr, 0, len(expr))
