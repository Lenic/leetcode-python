from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans, prev = 0, prices[0]
        for i in range(1, len(prices)):
            ans = max(ans, prices[i] - prev)
            prev = min(prev, prices[i])
        return ans


# 5
print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))

# 0
print(Solution().maxProfit([7, 6, 4, 3, 1]))
