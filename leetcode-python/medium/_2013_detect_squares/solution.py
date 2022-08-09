from typing import List, Tuple, Dict


class DetectSquares:
    """
    Maintain the frequency of all the points in a hash map.
    Traverse the hash map and if any point has the same x-coordinate as the query point,
    consider this point and the query point to form one of the vertical lines of the square.
    (consider left-side and right side)
    """
    freq: Dict[Tuple[int, int], int]

    def __init__(self):
        self.freq = {}

    def add(self, point: List[int]) -> None:
        p = (point[0], point[1])
        if p not in self.freq:
            self.freq[p] = 0
        self.freq[p] = self.freq[p] + 1

    def count(self, point: List[int]) -> int:
        num_square = 0
        for x, y in self.freq.keys():
            if x == point[0] and y != point[1]:
                square_length = abs(y - point[1])
                # check 2 points to the left
                lp1 = (point[0] - square_length, point[1])
                lp2 = (x - square_length, y)
                if lp1 in self.freq and lp2 in self.freq:
                    num_square += self.freq[(x, y)]*self.freq[lp1]* self.freq[lp2]

                # check 2 points to the right
                rp1 = (point[0] + square_length, point[1])
                rp2 = (x + square_length, y)
                if rp1 in self.freq and rp2 in self.freq:
                    num_square += self.freq[(x, y)] * self.freq[rp1]* self.freq[rp2]
        return num_square
