from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ans: int = 0

        def dfs(sum: int, i: int, rest: int):
            if i == len(nums):
                if sum == target:
                    nonlocal ans
                    ans += 1
                return

            val = sum - target
            if val < -rest or val > rest:
                return

            dfs(sum + nums[i], i + 1, rest - nums[i])
            dfs(sum - nums[i], i + 1, rest + nums[i])

        dfs(0, 0, sum(nums))
        return ans


# 5
print(Solution().findTargetSumWays(nums=[1, 1, 1, 1, 1], target=3))

# 5975
print(
    Solution().findTargetSumWays(
        nums=[22, 36, 7, 44, 38, 32, 16, 32, 1, 16, 25, 45, 49, 45, 27, 9, 41, 31, 10, 15], target=1
    )
)

# 6184
print(
    Solution().findTargetSumWays(
        nums=[27, 33, 4, 43, 31, 44, 47, 6, 6, 11, 39, 37, 15, 16, 8, 19, 48, 17, 18, 39], target=24
    )
)
