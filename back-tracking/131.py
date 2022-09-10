from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        status = [[True] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                status[i][j] = (s[i] == s[j]) and status[i + 1][j - 1]

        res: List[List[str]] = []
        ans: List[str] = []

        def dfs(i: int):
            if i == n:
                res.append(ans[:])
                return

            for j in range(i, n):
                if status[i][j]:
                    ans.append(s[i : j + 1])
                    dfs(j + 1)
                    ans.pop()

        dfs(0)
        return res


# [["a","a","b"],["aa","b"]]
print(Solution().partition("aab"))
