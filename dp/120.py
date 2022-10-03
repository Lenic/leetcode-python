from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ans = triangle[0][:]
        for i in range(1, len(triangle)):
            ans = [
                (min(ans[k] for k in range(max(j - 1, 0), min(j + 1, len(ans)))) + triangle[i][j])
                for j in range(len(triangle[i]))
            ]
        return min(ans)


# 11
print(Solution().minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
