from typing import List

class Solution:
    def solve(self, values: List[int], weights: List[int], capacity: int):
        """
        dp table - all the possible weights from 1 to W serve as columns
        dp table - all weights are kept as the rows
        :param values:
        :param weights:
        :param capacity:
        :return:
        """
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


class Solution4:
    '''
    Brute force
    '''
    def solve(self, values: List[int], weights: List[int], capacity: int) -> int:
        n = len(values)
        # padding
        values.insert(0, 0)
        weights.insert(0, 0)
        return self.ks(values, weights, capacity, n)

    def ks(self, values, weights, c, n):
        # base case
        if n == 0 or c == 0:
            return 0

        # current weight larger then capacity left
        if weights[n] > c:
            # cannot put item in, move to next item
            return self.ks(values, weights, c, n-1)
        else:
            # dont put
            value1 = self.ks(values, weights, c, n-1)
            # put
            value2 = values[n] + self.ks(values, weights, c - weights[n], n -1)
            return max(value1, value2)


class Solution5:
    '''
    Memorization
    '''

    def solve(self, values: List[int], weights: List[int], capacity: int) -> int:
        n = len(values)
        dp = [[None] * (capacity+1) for _ in range(n+1)]
        # padding
        values.insert(0, 0)
        weights.insert(0, 0)

        return self.ks(values, weights, capacity, n, dp)

    def ks(self, values, weights, c, n, dp):
        if dp[n][c] is not None:
            return dp[n][c]

        result = 0
        # base case
        if n == 0 or c == 0:
            result = 0
        elif weights[n] > c:
            result = self.ks(values, weights, c, n - 1, dp)
        else:
            # dont put
            value1 = self.ks(values, weights, c, n - 1, dp)
            # put
            value2 = values[n] + self.ks(values, weights, c - weights[n], n - 1, dp)
            result = max(value1, value2)

        # cache
        dp[n][c] = result
        return result


class Solution6:
    """
    Memorization
    """
    def solve(self, values: List[int], weights: List[int], capacity: int) -> int:
        # create array to remember optimal value of pair [n][c]
        n = len(values) - 1
        arr = [[None for _ in range(capacity+1)] for _ in range(len(values))]

        def helper(n: int, capacity: int):
            if arr[n][capacity] is not None:
                return arr[n][capacity]

            if n < 0 or capacity < 0:
                result = 0
            elif weights[n] > capacity:
                # not enough weight, more pointer to the left
                result = helper(n - 1, capacity)
            else:
                # pick item at n-th
                tmp1 = values[n] + helper(n - 1, capacity - weights[n])
                # not pick
                tmp2 = helper(n - 1, capacity)
                result = max(tmp1, tmp2)

            arr[n][capacity] = result
            return result

        return helper(n, capacity)




class Solution7:
    def solve(self, values: List[int], weights: List[int], capacity: int) -> int:
        pass
