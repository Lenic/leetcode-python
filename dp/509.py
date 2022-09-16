from typing import Callable, List


class Solution:
    def fib(self, n: int) -> int:
        data: List[int] = [-1] * (n + 1)

        def exec(func: Callable[[int], int]) -> Callable[[int], int]:
            def inner(cur: int) -> int:
                if data[cur] != -1:
                    return data[cur]

                res = func(cur)
                data[cur] = res
                return res

            return inner

        @exec
        def dp(cur: int) -> int:
            if cur == 0:
                return 0
            if cur == 1:
                return 1
            return dp(cur - 1) + dp(cur - 2)

        return dp(n)


# 1
print(Solution().fib(2))

# 3
print(Solution().fib(4))
