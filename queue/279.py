from typing import List

from collections import deque


class Solution:
    def numSquares(self, n: int) -> int:
        squares: List[int] = []
        for i in range(1, n + 1):
            val = i**2
            # 如果没有超过就继续添加完全平方数
            if val < n:
                squares.append(val)
            # 如果超过了就停止不再添加
            elif val > n:
                break
            # 如果等于就说明目标数就是个完全平方数，直接返回 1 即可
            else:
                return 1
        step, q, visited = 0, deque([0]), {0}
        while q:
            step += 1
            for i in range(len(q)):
                val = q.popleft()
                for s in squares:
                    cur = val + s
                    if cur < n and cur not in visited:
                        q.append(cur)
                        visited.add(cur)
                    if cur == n:
                        return step
        return -1


# 4
print(Solution().numSquares(7168))

# 1
print(Solution().numSquares(1))

# 3
print(Solution().numSquares(12))

# 2
print(Solution().numSquares(13))

# 1
print(Solution().numSquares(16))
