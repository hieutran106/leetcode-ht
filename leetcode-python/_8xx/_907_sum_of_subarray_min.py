import unittest
from typing import List

# Date: 2025-16-07

def next_less_elements(arr: List[int]):
    # next_less[i] = j means A[j] is the next less element of A[i].
    # next_less[i] = -1 means there is no next less element of A[i].
    ans = [-1] * len(arr)
    stack = [] # increasing stack
    for i, n in enumerate(arr):
        while stack and n < stack[-1][0]:
            item = stack.pop()
            ans[item[1]] = i
        stack.append((n, i))
    return ans

def prev_less_elements(arr: List[int]):
    ans = [-1] * len(arr)
    stack = [] # using increasing stack
    for i, n in enumerate(arr):
        while stack and n < stack[-1][0]:
            stack.pop()
        if stack:
            ans[i] = stack[-1][1]
        stack.append((n, i))
    return ans

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # instead of focusing on each subarray, think about how many times arr[i] is the min in a subarray
        # a[i] contribute to the answer a[i] * l * r
        next_less = next_less_elements(arr)
        prev_less = prev_less_elements(arr)
        mod = 10 ** 9 + 7
        ans = 0
        for i,n in enumerate(arr):
            # r: distance between A[i] and its next_less_element, including A[i], excluding NLE
            r = next_less[i] - i if next_less[i] != -1 else len(arr) - i
            # l: distance between A[i] and its prev_less_element, including A[i], excluding PLE
            l = i - prev_less[i] if prev_less[i] != -1 else i + 1
            print(f"At {i=} => {l=},{r=}")
            ans = (ans + n * l * r) % mod
        return ans

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_next_less_elements(self):
        actual = next_less_elements([3, 7, 8, 4])
        self.assertEqual([-1, 3, 3, -1], actual)

    def test_prev_less_elemets(self):
        actual = prev_less_elements([3, 7, 8, 4])
        self.assertEqual([-1, 0, 1, 0], actual)

    def test_case_6(self):
        actual = self.s.sumSubarrayMins([3, 7, 8, 4])
        self.assertEqual(46, actual)

    def test_case1(self):
        actual = self.s.sumSubarrayMins([3, 1, 2, 4])
        self.assertEqual(17, actual)

    def test_case2(self):
        actual = self.s.sumSubarrayMins([1, 2])
        self.assertEqual(4, actual)

    def test_case3(self):
        actual = self.s.sumSubarrayMins([1])
        self.assertEqual(1, actual)

    def test_case4(self):
        actual = self.s.sumSubarrayMins([3, 2, 2, 3])
        self.assertEqual(22, actual)

    def test_case5(self):
        actual = self.s.sumSubarrayMins([71, 55, 82, 55])
        self.assertEqual(593, actual)

if __name__ == '__main__':
    unittest.main()

