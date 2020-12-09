from typing import List

class Solution:
    def solve(self, values: List[int], weights: List[int], capacity: int):
        rows = len(values) + 1
        cols = capacity + 1
        dp = [[0] * cols for _ in range(rows)]
        for i in range(1, rows):
            for c in range(1, cols):
                profit1 = dp[i - 1][c]

                profit2 = 0
                curr_weight = weights[i - 1]
                if curr_weight <= c:
                    profit2 = values[i - 1] + dp[i-1][c - curr_weight]

                # compare
                dp[i][c] = max(profit1, profit2)

        self.trace_back(dp, values, weights, capacity)
        return dp[rows-1][cols-1]

    def trace_back(self, dp, values, weights, capacity):
        row = len(values)
        col = capacity
        # trace back to row 0
        while row != 0:
            # check if current item is selected
            if dp[row][col] == dp[row - 1][col]:
                # not select current item
                row = row - 1
                col = col
            else:
                # select current item
                print(f"Select item {row}, weight={weights[row-1]}, value={values[row-1]}")
                col = col - weights[row - 1]
                row = row - 1




class Solution3:
    '''
    Bruce force solution
    '''

    def solve(self, values: List[int], weights: List[int], capacity: int) -> int:
        # start from item 0
        return self.knapsack_recursive(values, weights, capacity, 0)

    def knapsack_recursive(self, values, weights, capacity, index) -> int:
        # base check
        if capacity < 0 or index >= len(values):
            return 0

        # include item at index
        profit1 = 0
        if weights[index] <= capacity:
            profit1 = values[index] + self.knapsack_recursive(values, weights, capacity - weights[index], index + 1)

        # not include item at index
        profit2 = self.knapsack_recursive(values, weights, capacity, index + 1)

        return max(profit1, profit2)
