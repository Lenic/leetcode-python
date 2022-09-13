from typing import List, Set


class Solution:
    def countArrangement(self, n: int) -> int:
        res: int = 0

        def dfs(ans: List[int]):
            if len(ans) == n:
                nonlocal res
                res += 1
                return

            index = len(ans) + 1
            for no in range(1, n + 1):
                if no in ans:
                    continue

                if (no % index == 0) or (index % no == 0):
                    ans.append(no)
                    dfs(ans)
                    ans.pop()

        dfs([])
        return res


# 3
print(Solution().countArrangement(3))

# 1
print(Solution().countArrangement(1))

# 2
print(Solution().countArrangement(2))
