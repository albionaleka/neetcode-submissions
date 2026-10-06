class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = prices[-1] - prices[0]

        for i in range(len(prices)):
            for j in range(len(prices)):
                if j > i and prices[j] - prices[i] > profit:
                    profit = prices[j] - prices[i]

        if profit < 0:
            profit = 0

        return profit
        