import random
import unittest


class RandomizedSet:

    def __init__(self):
        # Use array to store data as array access is 0(1) and removing last element is O(1)
        self.data = []
        # Store index
        self.idx = {}

    def insert(self, val: int) -> bool:
        if val in self.idx:
            return False
        self.data.append(val)
        self.idx[val] = len(self.data) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.idx:
            return False
        index = self.idx[val]

        last_element = self.data[-1]
        self.data[index] = last_element
        self.idx[last_element] = index
        self.data.pop()
        del self.idx[val]
        return True

    def getRandom(self) -> int:
        res = random.choice(self.data)
        return res

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = RandomizedSet()
    
    def test_case_1(self):
        randomizedSet = RandomizedSet()
        randomizedSet.insert(1)
        self.assertEqual(False, randomizedSet.remove(2))
        self.assertEqual(True, randomizedSet.insert(2))
        self.assertEqual(True, randomizedSet.getRandom() in [1, 2])

        self.assertEqual(True, randomizedSet.remove(1))
        self.assertEqual(False, randomizedSet.insert(2))
        self.assertEqual(2, randomizedSet.getRandom())

    def test_case_2(self):
        randomizedSet = RandomizedSet()

        self.assertEqual(False, randomizedSet.remove(0))
        self.assertEqual(False, randomizedSet.remove(0))
        self.assertEqual(True, randomizedSet.insert(0))
        self.assertEqual(0, randomizedSet.getRandom())
        self.assertEqual(True, randomizedSet.remove(0))
        self.assertEqual(False, randomizedSet.remove(0))

    def test_case_3(self):
        randomizedSet = RandomizedSet()

        self.assertEqual(True, randomizedSet.insert(0))
        self.assertEqual(True, randomizedSet.insert(1))
        self.assertEqual(True, randomizedSet.remove(0))
        self.assertEqual(True, randomizedSet.insert(2))
        self.assertEqual(True, randomizedSet.remove(1))
        self.assertEqual(2, randomizedSet.getRandom())





if __name__ == '__main__':
    unittest.main()

