import unittest
from typing import List


class ProductOfNumbers:

    def __init__(self):
        self.products = []

    def add(self, num: int) -> None:
        for i in range(len(self.products)):
            self.products[i] = self.products[i] * num
        self.products.append(num)

    def getProduct(self, k: int) -> int:
        return self.products[-k]


class MyTestCase(unittest.TestCase):

    def test_case_1(self):
        p = ProductOfNumbers()
        p.add(3)
        p.add(0)
        p.add(2)
        p.add(5)
        p.add(4)
        self.assertEqual(20, p.getProduct(2))
        self.assertEqual(40, p.getProduct(3))
        self.assertEqual(0, p.getProduct(4))
        p.add(8)
        self.assertEqual(32, p.getProduct(2))

    def test_case_2(self):
        p = ProductOfNumbers()
        p.add(1)
        p.add(1)
        p.add(1)
        self.assertEqual(1, p.getProduct(1))
        p.add(9)
        self.assertEqual(9, p.getProduct(4))

    def test_case_3(self):
        p = ProductOfNumbers()
        p.add(1)
        p.add(1)
        p.add(1)
        self.assertEqual(1, p.getProduct(1))
        p.add(0)
        self.assertEqual(0, p.getProduct(4))

    def test_case_4(self):
        p = ProductOfNumbers()
        p.add(1)
        p.add(1)
        self.assertEqual(1, p.getProduct(1))
        p.add(0)
        self.assertEqual(0, p.getProduct(1))
        p.add(1)
        self.assertEqual(1, p.getProduct(1))
        self.assertEqual(0, p.getProduct(2))
        self.assertEqual(0, p.getProduct(3))

if __name__ == '__main__':
    unittest.main()
