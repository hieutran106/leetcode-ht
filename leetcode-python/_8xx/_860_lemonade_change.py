import unittest
from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_count, ten_count, twenty_count = 0, 0, 0
        for b in bills:
            if b == 5:
                five_count += 1
            elif b == 10:
                ten_count += 1
                if five_count >= 1:
                    five_count -= 1
                else:
                    print(f"Got {b=} {five_count=} {ten_count=} {twenty_count=}")
                    return False
            elif b == 20:
                twenty_count += 1
                if five_count >= 1 and ten_count >= 1:
                    ten_count -= 1
                    five_count -= 1
                elif five_count >= 3:
                    five_count -= 3
                else:
                    print(f"Got {b=} {five_count=} {ten_count=} {twenty_count=}")
                    return False
            else:
                print("Something went wrong")
        return True

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.lemonadeChange(bills = [5,5,5,10,20])
        self.assertEqual(True, actual)
        
    def test_case_2(self):
        actual = self.s.lemonadeChange(bills = [5,5,10,10,20])
        self.assertEqual(False, actual)

    def test_case_3(self):
        with open("./_860_lemonade_change_test.txt", "r") as f:
            text = f.read()
            bills = []
            for num in text.split(","):
                bills.append(int(num))
            actual = self.s.lemonadeChange(bills)
            self.assertEqual(True, actual)



if __name__ == '__main__':
    unittest.main()

