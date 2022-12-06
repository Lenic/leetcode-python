from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans: List[List[int]] = [[1]]
        for _ in range(numRows - 1):
            cur, next = ans[-1], [1]
            for i in range(1, len(cur)):
                next.append(cur[i - 1] + cur[i])
            next.append(1)
            ans.append(next)
        return ans


# [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
print(Solution().generate(5))
