# O(n) time: iterate through the array once
# O(1) space: just need to keep the variable values

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        print(prices)
        
        minPrice = float('inf')
        profit = 0
        
        for price in prices:
            minPrice = min(price, minPrice)
            profit = max(profit, price - minPrice)
            # print(minPrice, profit, maxProfit)
        
        return profit