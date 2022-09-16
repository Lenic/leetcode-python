from typing import List, MutableSet


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res: List[int] = []
        cache: MutableSet[str] = set()

        def dfs(ans: List[int]):
            if len(ans) != 1:
                cacheKey = "-".join(str(ans[i]) for i in range(1, len(ans)))
                if cacheKey in cache:
                    return
                cache.add(cacheKey)

            if len(ans) == n + 1:
                num = 0
                for i in range(1, len(ans)):
                    num = num * 10 + ans[i]
                res.append(num)
                return

            for val in [ans[-1] - k, ans[-1] + k]:
                if 0 <= val <= 9:
                    if len(ans) == 1 and val == 0:
                        continue
                    ans.append(val)
                    dfs(ans)
                    ans.pop()

        for val in range(1 - k, 10 - k):
            dfs([val])
        return res


# [181,292,707,818,929]
print(Solution().numsSameConsecDiff(3, 7))

# [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
print(Solution().numsSameConsecDiff(2, 1))
