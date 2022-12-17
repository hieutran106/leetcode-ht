from typing import List

class Solution2:
    def longestMountain(self, arr: List[int]) -> int:
        i = mountain = 0
        n = len(arr)
        while i < n:
            base = i
            # walk up
            while i < n - 1 and arr[i+1] > arr[i]:
                i += 1

            if i == base:
                i += 1
                continue
            peek = i
            # walk down
            while i < n - 1 and arr[i+1] < arr[i]:
                i += 1

            if i == peek:
                i += 1
                continue
            mountain = max(mountain, i - base + 1)

        return mountain

























class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0
        peek = 1
        mountain = 0
        while peek < n - 1:
            print("============")
            print(f"Process {peek=}, value={arr[peek]}")
            left = peek
            while left > 0 and arr[left-1] < arr[left]:
                left -= 1
            if left == peek:
                print("LEFT not found")
                peek += 1
                continue

            right = peek
            while right < n - 1 and arr[right+1] < arr[right]:
                right += 1
            if right == peek:
                print(f"RIGHT not found.")
                peek += 1
                continue

            mountain = max(mountain, right - left + 1)
            print(f"With {left=} and {right=} => {mountain=}")
            print(f"Move peek to right, {right=}")
            peek = right + 1
        return mountain

