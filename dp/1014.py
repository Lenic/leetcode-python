from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res, previous = 0, values[0]
        for i in range(1, len(values)):
            res = max(res, previous + values[i] - i)
            previous = max(previous, values[i] + i)
        return res


# 11
print(Solution().maxScoreSightseeingPair([8, 1, 5, 2, 6]))

# 2
print(Solution().maxScoreSightseeingPair([1, 2]))
