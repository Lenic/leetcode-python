from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        s = sum(matchsticks)
        if s % 4:
            return False
        matchsticks.sort(reverse=True)

        edges = [0] * 4
        edgeLen = s // 4

        def dfs(index: int):
            if index == len(matchsticks):
                return True

            # push the first edge if it's the first
            for i in range(1 if index == 0 else 4):
                # skip if both edges is equal
                if i > 0 and edges[i] == edges[i - 1]:
                    continue
                # skip if the sum great than target edge length
                if edges[i] + matchsticks[index] > edgeLen:
                    continue

                edges[i] += matchsticks[index]
                if dfs(index + 1):
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
