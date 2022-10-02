from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1] * (rowIndex + 1)
        for i in range(2, len(ans)):
            previous = 1
            for j in range(1, i):
                ans[j], previous = previous + ans[j], ans[j]
        return ans


# [1,3,3,1]
print(Solution().getRow(3))

# [1,4,6,4,1]
print(Solution().getRow(4))
