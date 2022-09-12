from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        totalLen = sum(matchsticks)
        if totalLen % 4:
            return False
        matchsticks.sort(reverse=True)

        edges = [0] * 4
        edgeLen = totalLen // 4

        def dfs(index: int) -> bool:
            if index == len(matchsticks):
                return True

            for i in range(4):
                edges[i] += matchsticks[index]
                if edges[i] <= edgeLen and dfs(index + 1):
                    return True
                edges[i] -= matchsticks[index]

            return False

        return dfs(0)


# True
print(Solution().makesquare([5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3]))

# True
print(Solution().makesquare([1, 1, 2, 2, 3, 3]))

# True
print(Solution().makesquare([1, 1, 2, 2, 2]))
