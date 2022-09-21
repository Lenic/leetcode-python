from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        res = positiveCount = negativeCount = 0
        for val in nums:
            if val > 0:
                positiveCount += 1
                negativeCount = (negativeCount + 1) if negativeCount > 0 else 0
            elif val < 0:
                if positiveCount > 0:
                    negativeCount, positiveCount = positiveCount + 1, (negativeCount + 1) if negativeCount > 0 else 0
                else:
                    negativeCount, positiveCount = 1, (negativeCount + 1) if negativeCount > 0 else 0
            else:
                positiveCount = negativeCount = 0
            res = max(res, positiveCount)
        return res


# 8
print(Solution().getMaxLen([5, -20, -20, -39, -5, 0, 0, 0, 36, -32, 0, -7, -10, -7, 21, 20, -12, -34, 26, 2]))

# 1
print(Solution().getMaxLen([-1, 2]))

# 0
print(Solution().getMaxLen([-1]))

# 1
print(Solution().getMaxLen([1]))

# 2
print(Solution().getMaxLen([-1, -2, -3, 0, 1]))

# 4
print(Solution().getMaxLen([1, -2, -3, 4]))

# 3
print(Solution().getMaxLen([0, 1, -2, -3, -4]))
