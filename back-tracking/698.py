from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        totalSum = sum(nums)
        if totalSum % k != 0:
            return False

        # 每个容器的目标和
        avg = totalSum // k
        # k 个容器
        containers = [0] * k
        # 按照数据的从大到小排列
        nums.sort(reverse=True)

        def dfs(index: int) -> bool:
            if index == len(nums):
                return True

            for i in range(1 if index == 0 else k):
                if i > 0 and containers[i] == containers[i - 1]:
                    continue

                containers[i] += nums[index]
                if containers[i] <= avg and dfs(index + 1):
                    return True
                containers[i] -= nums[index]

            return False

        return dfs(0)


# True
print(
    Solution().canPartitionKSubsets(
        [730, 580, 401, 659, 5524, 405, 1601, 3, 383, 4391, 4485, 1024, 1175, 1100, 2299, 3908], 4
    )
)

# False
print(Solution().canPartitionKSubsets([1, 2, 3, 4], 3))

# True
print(Solution().canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))
