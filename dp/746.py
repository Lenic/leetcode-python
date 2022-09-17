from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        left, right = 0, 0
        for i in range(2, len(cost) + 1):
            left, right = right, min(left + cost[i - 2], right + cost[i - 1])
        return right


# 15
print(Solution().minCostClimbingStairs([10, 15, 20]))

# 6
print(Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
