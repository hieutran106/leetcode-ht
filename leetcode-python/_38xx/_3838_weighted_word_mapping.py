import unittest
from typing import List

# Date: 2026-06-14
# Problem: 3838 weighted_word_mapping
class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = []
        for word in words:
            weight = 0
            for c in word:
                weight += weights[ord(c) - ord('a')]
            result = weight % 26
            char = chr((25-result) + ord('a'))
            print(f"{word=}, {result=}, {char=}")
            ans.append(char)
        return "".join(ans)
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.mapWordWeights(words = ["abcd","def","xyz"], weights = [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2])
        self.assertEqual(actual, "rij")

        
    def test_case_2(self):
        actual = self.s.mapWordWeights(words = ["a","b","c"], weights = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
        self.assertEqual(actual, "yyy")

    def test_case_3(self):
        actual = self.s.mapWordWeights(words = ["abcd"], weights = [7,5,3,4,3,5,4,9,4,2,2,7,10,2,5,10,6,1,2,2,4,1,3,4,4,5])
        self.assertEqual(actual, "g")


if __name__ == '__main__':
    unittest.main()

