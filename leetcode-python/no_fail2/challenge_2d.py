import sys
from typing import List


def solve(numbers, k):
    result = []
    for i in range(1, len(numbers)):
        result.append(numbers[i] - numbers[i-1])
    y = sorted(result, reverse=True)
    z = filter(lambda x: x > 0, y[:k])
    print(sum(z))


def solve2(numbers, k):
    my_stack = []
    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i-1]
        if len(my_stack) > 0 and my_stack[-1] > 0 and diff > 0:
            top = my_stack.pop()
            my_stack.append(diff + top)
        else:
            my_stack.append(diff)

    y = sorted(my_stack, reverse=True)
    z = list(filter(lambda x: x > 0, y[:k]))
    result = sum(z)
    print(result)
    return result

def maxProfit(prices: List[int], k: int) -> int:
    n = len(prices)
    if k == 0 or n ==0:
        return 0
    rows = 2 * k
    dp = [[float('-inf') for _ in range(len(prices))] for _ in range(rows)]
    dp[0][0] = - prices[0]

    for i in range(1, n):
        for j in range(rows):
            if j == 0:
                dp[0][i] = max(dp[0][i - 1], -prices[i])
            elif j % 2 == 1:
                dp[j][i] = max(dp[j][i - 1], dp[j-1][i] + prices[i])
            else:
                dp[j][i] = max(dp[j][i - 1], dp[j - 1][i] - prices[i])

    res = 0
    for j in range(rows):
        if dp[j][n-1] > res:
            res = dp[j][n-1]

    return res


if __name__ == "__main__":
    lines = [line.rstrip() for line in sys.stdin.readlines()]
    n_k = list(map(int, lines[0].split(' ')))
    k = n_k[1]
    numbers = list(map(int, lines[1].split(' ')))
    result = maxProfit(numbers, k)
    print(result)