
## Basic Dynamic programming solution

dp[i] will denote the maximum score that we can obtain from i-th index
So we have:
```python
start = max(0, i - k)
end = i
dp[i] = max(dp[start:end]) + nums[i]
```
Time complexity: O(n*k)
This solution leads to TLE

## Optimized version
Use a monotonic queue, a decreasing queue to be precise, to look up `max(dp[start:end])` in `O(1)`. Th maximum value is `deque[0]`.

Before appending an element to the queue, we remove all smaller values. For example:

`deque([5, 2, 1]) - append(3) --> deque([5, 3]). Pop 2, 1`

`deque([5, 3]) - append(4) --> deque([5, 4]). Pop 3`

In this solution, we store (value, index) as queue element. We will also pop the element if the index is out of range `i - k`