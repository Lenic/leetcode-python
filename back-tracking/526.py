from typing import List, Set


class Solution:
    def countArrangement(self, n: int) -> int:
        res: int = 0
        visited = [False] * (n + 1)

        def dfs(ans: List[int]):
            if len(ans) == n:
                nonlocal res
                res += 1
                return

            index = len(ans) + 1
            for no in range(1, n + 1):
                if visited[no]:
                    continue

                if (no % index == 0) or (index % no == 0):
                    visited[no] = True
                    ans.append(no)
                    dfs(ans)
                    ans.pop()
                    visited[no] = False

        dfs([])
        return res


# 3
print(Solution().countArrangement(3))

# 1
print(Solution().countArrangement(1))

# 2
print(Solution().countArrangement(2))
