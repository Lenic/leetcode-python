class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:

        w = maxPts
        if n >= k + w - 1:  # 最大点数<=n，则一定能赢
            return 1

        dp: list[float] = [0] * (k + w)  # 动态规划初始值

        # 将能赢得游戏的点数概率设为1
        for i in range(k, n + 1):  # 此时 n<k+w-1
            dp[i] = 1  # [k, n]内的点数获胜概率为1
        window_sum = n - k + 1  # 概率为1的状态总数

        # 滑动窗口【从 k-1 开始往左滑】
        for i in range(k - 1, -1, -1):
            dp[i] = window_sum / w
            window_sum = window_sum - dp[i + w] + dp[i]

        return dp[0]


# 1.00000
print(Solution().new21Game(n=10, k=1, maxPts=10))
