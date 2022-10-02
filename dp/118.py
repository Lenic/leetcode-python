from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 首先初始化第一层
        res: List[List[int]] = [[1]]
        # 从第二层开始循环处理
        for _ in range(2, numRows + 1):
            ans = []
            previous = 0
            for val in res[-1]:
                ans.append(previous + val)
                previous = val
            ans.append(1)
            res.append(ans)
        return res


# [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
print(Solution().generate(5))
