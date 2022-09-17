class Solution:
    def climbStairs(self, n: int) -> int:
        res: int = 0

        def dfs(rest: int):
            if rest < 0:
                return
            if rest == 0:
                nonlocal res
                res += 1
                return

            dfs(rest - 1)
            dfs(rest - 2)

        dfs(n)
        return res


# 2
print(Solution().climbStairs(2))

# 3
print(Solution().climbStairs(3))

# 5
print(Solution().climbStairs(4))
