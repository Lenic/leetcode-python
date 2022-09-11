from typing import List


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10

        res: int = 0

        def dfs(ans: List[int], level: int):
            if level == n:
                nonlocal res
                res += 1
                return

            for i in range(1 if level == 0 else 0, 10):
                if i in ans:
                    continue

                ans.append(i)
                dfs(ans, level + 1)
                ans.pop()

        dfs([], 0)
        return res + self.countNumbersWithUniqueDigits(n - 1)


# 91
print(Solution().countNumbersWithUniqueDigits(2))

# 739
print(Solution().countNumbersWithUniqueDigits(3))
