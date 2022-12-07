from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        cur = [1]
        for _ in range(rowIndex):
            next = [1]
            for i in range(1, len(cur)):
                next.append(cur[i - 1] + cur[i])
            next.append(1)
            cur = next
        return cur


# [1, 3, 3, 1]
print(Solution().getRow(3))
