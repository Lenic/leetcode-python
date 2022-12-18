from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans: int = 0
        i, j = 0, len(height) - 1
        while i < j:
            ans = max(ans, min(height[i], height[j]) * (j - i))
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return ans


# 49
print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
