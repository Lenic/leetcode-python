from typing import List, Tuple


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans: List[int] = [0] * len(temperatures)
        stack: List[Tuple[int, int]] = []
        for index, val in enumerate(temperatures):
            while len(stack) and stack[-1][1] < val:
                previousIndex, _ = stack.pop()
                ans[previousIndex] = index - previousIndex
            stack.append((index, val))
        return ans


# [1,1,4,2,1,1,0,0]
print(Solution().dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]))

# [1,1,1,0]
print(Solution().dailyTemperatures(temperatures=[30, 40, 50, 60]))

# [1,1,0]
print(Solution().dailyTemperatures(temperatures=[30, 60, 90]))
