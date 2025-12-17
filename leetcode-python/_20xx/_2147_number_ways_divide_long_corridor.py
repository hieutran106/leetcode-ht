import unittest
from typing import List

# Date: 2025-12-16
# Problem: 2147 number_ways_divide_long_corridor
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        seat_count = 0
        for c in corridor:
            if c == 'S':
                seat_count+= 1
        if seat_count==0 or seat_count % 2 == 1:
            return 0

        seat_count = 0
        plant_count = 0
        MOD = 10 ** 9 + 7
        res = []
        for i, v in enumerate(corridor):
            if seat_count < 2 and v == 'S':
                seat_count += 1
            elif seat_count == 2 and v == 'P':
                plant_count += 1
            elif seat_count == 2 and v == 'S':
                seat_count = 1
                res.append(plant_count)
                plant_count = 0

        ans = 1
        for c in res:
            ans = (ans * (c + 1)) % MOD
        return ans

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.numberOfWays(corridor = "SSPPSPS")
        self.assertEqual(3, actual)
        
    def test_case_2(self):
        actual = self.s.numberOfWays(corridor = "PPSPSP")
        self.assertEqual(1, actual)

    def test_case_3(self):
        actual = self.s.numberOfWays(corridor = "S")
        self.assertEqual(0, actual)

    def test_case_4(self):
        actual = self.s.numberOfWays(corridor = "P")
        self.assertEqual(0, actual)

    def test_case_5(self):
        actual = self.s.numberOfWays(corridor = "SPPSPPSSPPPSSPPP")
        self.assertEqual(12, actual)

    def test_case_6(self):
        actual = self.s.numberOfWays(corridor = "SPPSPPSSPPPSPPPS")
        self.assertEqual(12, actual)

    def test_case_7(self):
        actual = self.s.numberOfWays(corridor = "PPPPPSPPSPPSPPPSPPPPSPPPPSPPPPSPPSPPPSPSPPPSPSPPPSPSPPPSPSPPPPSPPPPSPPPSPPSPPPPSPSPPPPSPSPPPPSPSPPPSPPSPPPPSPSPSS")
        self.assertEqual(919999993, actual)

if __name__ == '__main__':
    unittest.main()

