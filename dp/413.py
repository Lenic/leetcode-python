from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        # 数量不够时直接返回 0
        if n < 3:
            return 0

        res, left, right, diff = 0, 0, 1, nums[1] - nums[0]
        while right < n:
            while right < n:
                right += 1
                if right == n:
                    break

                currentDiff = nums[right] - nums[right - 1]
                if currentDiff != diff:
                    diff = currentDiff
                    break

            count = right - left
            if count >= 3:
                # 计算这个区间段产生的等差数组数量
                fragmentCount = 0
                for i in range(3, count + 1):
                    # 根据数学规律得出算式
                    fragmentCount += count - i + 1
                # 将当前段的等差数组数量添加到结果中
                res += fragmentCount
            # 重新设置 left 为最后一个符合 diff 的索引
            left = right - 1
        return res


# 0
print(Solution().numberOfArithmeticSlices([1]))

# 6
print(Solution().numberOfArithmeticSlices([1, 3, 5, 7, 9]))

# 3
print(Solution().numberOfArithmeticSlices([1, 2, 3, 4]))

# 3
print(Solution().numberOfArithmeticSlices([7, 7, 7, 7]))
