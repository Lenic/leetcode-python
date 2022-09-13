from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res: int = 0
        n = len(nums)

        def dfs(index: int, prefixSum: int):
            if index == n:
                if prefixSum == target:
                    nonlocal res
                    res += 1
                return

            dfs(index + 1, prefixSum + nums[index])
            dfs(index + 1, prefixSum - nums[index])

        dfs(0, 0)
        return res


# 5
print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))

# 6692
print(Solution().findTargetSumWays([6, 44, 30, 25, 8, 26, 34, 22, 10, 18, 34, 8, 0, 32, 13, 48, 29, 41, 16, 30], 12))

# 5798
print(Solution().findTargetSumWays([11, 19, 14, 50, 47, 35, 18, 32, 8, 2, 31, 45, 6, 25, 49, 23, 25, 33, 24, 33], 44))
