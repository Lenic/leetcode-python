class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1

        v0, v1, v2 = 0, 1, 1
        for _ in range(3, n + 1):
            val = v0 + v1 + v2
            v0, v1, v2 = v1, v2, val
        return v2


# 4
print(Solution().tribonacci(4))

# 1389537
print(Solution().tribonacci(25))
