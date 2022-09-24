from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = left = right = int(0)
        while right < len(prices) - 1:
            for i in range(left + 1, len(prices)):
                right = i
                # 当天股票的价格小于等于昨天
                if prices[right] <= prices[right - 1]:
                    # 递增区间停止，并且时间间隔大于 1 天时，表示昨天是卖出的最佳时机
                    if right - left - 1 > 0:
                        # 累积获得的利润
                        res += prices[right - 1] - prices[left]
                    # 开启新的一轮计算
                    left = right
        return res if left == right else res + prices[right] - prices[left]


# 7
print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))

# 4
print(Solution().maxProfit([1, 2, 3, 4, 5]))

# 0
print(Solution().maxProfit([7, 6, 4, 3, 1]))
