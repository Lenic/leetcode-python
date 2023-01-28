from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans: List[List[int]] = [[1]]
        for i in range(2, numRows + 1):
            prev, cur = ans[-1], [1] * i
            for j in range(1, len(prev)):
                cur[j] = prev[j - 1] + prev[j]
            ans.append(cur)
        return ans


# [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
print(Solution().generate(5))
