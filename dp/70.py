class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        left, right = 1, 2
        for _ in range(3, n):
            left, right = right, left + right
        return left + right


# 2
print(Solution().climbStairs(2))

# 3
print(Solution().climbStairs(3))

# 1836311903
print(Solution().climbStairs(45))
