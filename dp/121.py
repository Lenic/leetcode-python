from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, previous = 0, prices[0]
        for i in range(1, len(prices)):
            res = max(res, prices[i] - previous)
            previous = min(previous, prices[i])
        return res if res > 0 else 0


# 5
print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))

# 0
print(Solution().maxProfit([7, 6, 4, 3, 1]))
