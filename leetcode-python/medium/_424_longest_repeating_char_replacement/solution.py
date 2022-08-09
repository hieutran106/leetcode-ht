class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Using a window and slide it in condition that
        len(window) - max(freqency) <= k
        if not, we shift window to the right
        (and we keep the window size, as we are interested in finding max)
        """
        # frequency of chars in a window
        freq = [0] * 26
        longest = 1
        left = right = 0

        while right < len(s):
            freq[ord(s[right]) - ord('A')] += 1
            window_len = right - left + 1
            if window_len - max(freq) <= k:
                longest = max(longest, window_len)
            else:
                freq[ord(s[left]) - ord('A')] -= 1
                left += 1
            right += 1

        return longest
