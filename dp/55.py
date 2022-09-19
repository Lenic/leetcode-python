from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # DP Table
        status = [False] * len(nums)
        # 初始化第一个值
        status[-1] = True
        # 从后往前计算
        for i in range(len(nums) - 2, -1, -1):
            val = i + nums[i]
            for j in range(min(val, len(nums) - 1), i, -1):
                if status[j]:
                    status[i] = True
                    break
        return status[0]


# True
print(Solution().canJump([4, 0, 0, 0, 4]))

# True
print(Solution().canJump([2, 3, 1, 1, 4]))

# False
print(Solution().canJump([3, 2, 1, 0, 4]))
