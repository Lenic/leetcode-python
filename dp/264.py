from typing import List

import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n <= 1:
            return n

        value = 1
        queue: List[int] = []
        cache: set[int] = set()

        for _ in range(n - 1):
            for val in [2, 3, 5]:
                targetValue = value * val
                if targetValue not in cache:
                    heapq.heappush(queue, targetValue)
                    cache.add(targetValue)
            value = heapq.heappop(queue)

        return value


# 5
print(Solution().nthUglyNumber(5))

# 12
print(Solution().nthUglyNumber(10))
