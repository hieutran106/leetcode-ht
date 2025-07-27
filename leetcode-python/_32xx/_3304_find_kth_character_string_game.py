import unittest
from typing import List
import math

# Date: 2025-03-07

def next_string(word: str):
    ans = ""
    for c in word:
        if c == 'z':
            ans += "a"
        else:
            ans += chr(ord(c) + 1)
    return ans

def cal():
    k_max = 500
    op = math.ceil(math.log(k_max)/ math.log(2))
    ans = "a"
    for i in range(0, op):
        ans = ans + next_string(ans)
        print(f"{i=}: {ans=}")
    return ans

cache = 'abbcbccdbccdcddebccdcddecddedeefbccdcddecddedeefcddedeefdeefeffgbccdcddecddedeefcddedeefdeefeffgcddedeefdeefeffgdeefeffgeffgfgghbccdcddecddedeefcddedeefdeefeffgcddedeefdeefeffgdeefeffgeffgfgghcddedeefdeefeffgdeefeffgeffgfgghdeefeffgeffgfggheffgfgghfgghghhibccdcddecddedeefcddedeefdeefeffgcddedeefdeefeffgdeefeffgeffgfgghcddedeefdeefeffgdeefeffgeffgfgghdeefeffgeffgfggheffgfgghfgghghhicddedeefdeefeffgdeefeffgeffgfgghdeefeffgeffgfggheffgfgghfgghghhideefeffgeffgfggheffgfgghfgghghhieffgfgghfgghghhifgghghhighhihiij'
class Solution:
    def kthCharacter(self, k: int) -> str:
        return cache[k-1]
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.kthCharacter(k = 5)
        self.assertEqual("b", actual)
        
    def test_case_2(self):
        actual = self.s.kthCharacter(k=10)
        self.assertEqual("c", actual)

if __name__ == '__main__':
    unittest.main()

