from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n < 2:
            return 0

        buy, none = -prices[0] - fee, 0
        for i in range(1, n):
            newNone = max(buy + prices[i], none)
            newBuy = max(buy, none - prices[i] - fee)
            buy, none = newBuy, newNone
        return max(buy, none)


# 8
print(Solution().maxProfit([1, 3, 2, 8, 4, 9], 2))

# 6
print(Solution().maxProfit([1, 3, 7, 5, 10, 3], 3))
