from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 只有一天时没有任何收益
        if len(prices) < 2:
            return 0

        # p1 表示持有股票的收益
        # p2 表示处于冻结期的收益
        # p3 表示非冻结期但是没有购入股票的收益
        p1, p2, p3 = -prices[0], 0, 0
        for i in range(1, len(prices)):
            # 当前持有股票的收益，两者取最大值
            # - 前一天就持有股票，今天继续持有的收益
            # - 前一天没有持有，但今天通过购买获得了股票
            np1 = max(p1, p3 - prices[i])
            # 当前处于冻结状态的收益
            # - 前一天持有股票，今天卖掉处于冻结期
            np2 = p1 + prices[i]
            # 当前没有持有股票，并且没有处于冻结期的收益
            # - 昨天处于冻结期
            # - 昨天没有处于冻结期，并且昨天没有买入股票
            np3 = max(p2, p3)
            # 将新值赋值给外部的变量
            p1, p2, p3 = np1, np2, np3
        return max(p2, p3)


# 3
print(Solution().maxProfit([1, 2, 3, 0, 2]))
