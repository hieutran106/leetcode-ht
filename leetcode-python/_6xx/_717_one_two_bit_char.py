import unittest
from lib2to3.btm_utils import reduce_tree
from typing import List

# Date: 2025-11-19
# Problem: 717 one_two_bit_char
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits) - 1:
            if bits[i] == 1:
                i += 2
                continue
            i += 1

        print(f"{len(bits) - 1}:{i=}")
        return i == len(bits) - 1
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.isOneBitCharacter(bits = [1,0,0])
        self.assertEqual(actual, True)
        
    def test_case_2(self):
        actual = self.s.isOneBitCharacter(bits = [1,1,1,0])
        self.assertEqual(actual, False)

    def test_case_3(self):
        actual = self.s.isOneBitCharacter(bits = [0])
        self.assertEqual(actual, True)

    def test_case_4(self):
        actual = self.s.isOneBitCharacter(bits = [1,0])
        self.assertEqual(actual, False)

    def test_case_5(self):
        actual = self.s.isOneBitCharacter(bits = [1, 1, 0, 0])
        self.assertEqual(actual, True)

    def test_case_6(self):
        actual = self.s.isOneBitCharacter(bits = [1])
        self.assertEqual(actual, True)

if __name__ == '__main__':
    unittest.main()

