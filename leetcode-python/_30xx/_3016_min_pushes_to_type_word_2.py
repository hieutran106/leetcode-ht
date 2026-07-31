import unittest
import collections
from typing import List

# Date: 2026-07-31
# Problem: 3016 min_pushes_to_type_word_2
class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = collections.Counter(word)
        sorted_counter = sorted(counter.items(), key=lambda item: item[1], reverse=True)
        print(sorted_counter)
        ans = 0
        key = 2
        pushes = 1
        for k,v in sorted_counter:
            ans += pushes * v
            key += 1
            if key > 9:
                key = 2
                pushes += 1

        return ans
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.minimumPushes(word = "abcde")
        self.assertEqual(5, actual)
        
    def test_case_2(self):
        actual = self.s.minimumPushes(word = "xyzxyzxyzxyz")
        self.assertEqual(12, actual)

    def test_case_3(self):
        actual = self.s.minimumPushes(word = "aabbccddeeffgghhiiiiii")
        self.assertEqual(24, actual)

if __name__ == '__main__':
    unittest.main()

