import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # dp[i] hold ugly number i-th
        dp = [1, 1]

        heap = [2, 3, 5]

        for i in range(2, n+1):
            min = heap[0]
            while len(heap) > 0 and heap[0] == min:
                heapq.heappop(heap)
            dp.append(min)
            heapq.heappush(heap, dp[i] * 2)
            heapq.heappush(heap, dp[i] * 3)
            heapq.heappush(heap, dp[i] * 5)

        return dp[n]



class Solution2:
    def nthUglyNumber(self, nth: int) -> int:
        if nth <= 5:
            return nth

        dp = [False, True, True, True, True, True]

        current_th = 5
        while True:
            if current_th == nth:
                break

            number = len(dp)
            if number % 2 == 0 and dp[number // 2] is True:
                dp.append(True)
                current_th += 1
            elif number % 3 == 0 and dp[number // 3] is True:
                dp.append(True)
                current_th += 1
            elif number % 5 == 0 and dp[number // 5] is True:
                dp.append(True)
                current_th += 1
            else:
                dp.append(False)

        return len(dp) - 1
