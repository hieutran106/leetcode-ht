from typing import List
import copy

'''
Given the array prices where prices[i] is the price of the ith item in a shop. 
There is a special discount for items in the shop, 
if you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i], 
otherwise, you will not receive any discount at all.
Return an array where the ith element is the final price you will pay for the ith item of the shop considering the special discount.
'''

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = copy.copy(prices)
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    discounted_price = prices[i] - prices[j]
                    if discounted_price <= result[i]:
                        result[i] = discounted_price
                        break

        return result