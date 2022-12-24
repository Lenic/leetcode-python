from typing import List

from collections import deque


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack: deque[tuple[int, int]] = deque([(0, temperatures[0])])
        for i in range(1, len(temperatures)):
            while len(stack) and stack[-1][1] < temperatures[i]:
                top = stack.pop()
                ans[top[0]] = i - top[0]
            stack.append((i, temperatures[i]))
        return ans


# [8,1,5,4,3,2,1,1,0,0]
print(Solution().dailyTemperatures([89, 62, 70, 58, 47, 47, 46, 76, 100, 70]))

# [1,1,1,0]
print(Solution().dailyTemperatures([30, 40, 50, 60]))

# [1,1,0]
print(Solution().dailyTemperatures([30, 60, 90]))

# [1,1,4,2,1,1,0,0]
print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
