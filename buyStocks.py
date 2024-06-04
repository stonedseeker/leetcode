class Solution:
    def maxProfit(self, prices):
        sum = 0
        for i, j in zip(range(0, len(prices) - 1), range(1, len(prices))):
            if prices[i] < prices[j]:
                sum += prices[j] - prices[i]
        print(sum)
        return sum


Solution().maxProfit([7, 1, 5, 3, 6, 4])
