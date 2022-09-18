from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        data = [0] * (max(nums) + 1)
        for val in nums:
            data[val] += val

        if len(data) == 2:
            return max(data)

        left, right = data[0], max(data[0], data[1])
        for i in range(2, len(data)):
            left, right = right, max(left + data[i], right)
        return right


# 1
print(Solution().deleteAndEarn([1]))

# 6
print(Solution().deleteAndEarn([3, 4, 2]))

# 9
print(Solution().deleteAndEarn([2, 2, 3, 3, 3, 4]))
