import unittest
from typing import List
import collections


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        counter1 = collections.Counter(s1.split(" "))
        counter2 = collections.Counter(s2.split(" "))
        ans = []
        for key, value in counter1.items():
            if key not in counter2 and value == 1:
                ans.append(key)

        for key, value in counter2.items():
            if key not in counter1 and value == 1:
                ans.append(key)
        return ans

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.uncommonFromSentences("s z z z s", "s z ejt")
        self.assertEqual(actual, ["ejt"])

    def test_case_2(self):
        actual = self.s.uncommonFromSentences("apple apple", "banana")
        self.assertEqual(actual, ["banana"])

    def test_case_3(self):
        actual = self.s.uncommonFromSentences("banana", "apple apple")
        self.assertEqual(actual, ["banana"])

if __name__ == '__main__':
    unittest.main()
