from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 1:
            return 0

        leftMaxes = [0] * (n + 1)
        for i in range(n):
            leftMaxes[i + 1] = max(leftMaxes[i], height[i])

        rightMaxes = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            rightMaxes[i] = max(rightMaxes[i + 1], height[i])

        return sum(min(leftMaxes[i + 1], rightMaxes[i]) - height[i] for i in range(n))


# 6
print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
