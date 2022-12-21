from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans: int = 0
        for i in range(1, len(prices)):
            ans += max(0, prices[i] - prices[i - 1])
        return ans


# 0
print(Solution().maxProfit([7, 6, 4, 3, 1]))

# 4
print(Solution().maxProfit([1, 2, 3, 4, 5]))

# 7
print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
