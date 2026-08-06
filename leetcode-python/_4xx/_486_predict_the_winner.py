import unittest
from typing import List

# Date: 2026-08-02
# Problem: 486 predict_the_winner
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        memo = {}
        def dp(turn, l, r, alice_score, bob_score):
            if l == r:
                if turn == "alice":
                    res = alice_score + nums[l] >= bob_score
                    return res
                else:
                    res = alice_score >= bob_score + nums[l]
                    return res
            if (turn, l, r, alice_score, bob_score) in memo:
                return memo[(turn, l, r, alice_score, bob_score)]
            if turn == "alice":
                c1 = dp("bob", l+1, r, alice_score + nums[l], bob_score)
                c2 = dp("bob", l, r - 1, alice_score + nums[r], bob_score)
                res = c1 or c2

            else:
                c1 = dp("alice", l+1, r, alice_score, bob_score + nums[l])
                c2 = dp("alice", l, r-1, alice_score, bob_score + nums[r])
                # alice must win in both case
                res = c1 and c2

            memo[(turn, l, r, alice_score, bob_score)] = res
            return res

        l, r = 0, len(nums) - 1
        ans = dp("alice", l, r, 0, 0)
        return ans
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.predictTheWinner(nums = [1,5,2])
        self.assertEqual(False, actual)
        
    def test_case_2(self):
        actual = self.s.predictTheWinner(nums = [1,5,233,7])
        self.assertEqual(True, actual)

    def test_case_3(self):
        actual = self.s.predictTheWinner(nums = [1])
        self.assertEqual(True, actual)

    def test_case_4(self):
        actual = self.s.predictTheWinner(nums = [0])
        self.assertEqual(True, actual)

    def test_case_5(self):
        actual = self.s.predictTheWinner(nums = [1, 2])
        self.assertEqual(True, actual)


if __name__ == '__main__':
    unittest.main()

