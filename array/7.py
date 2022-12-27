class Solution:
    min = -(2**31)
    max = 2**31 - 1
    top = (2**31 - 1) // 10
    positiveRemainder = 7
    negativeRemainder = 8

    def reverse(self, x: int) -> int:
        ans, rest, isNegative = 0, x, False
        if x < 0:
            if x < self.min:
                return ans
            rest, isNegative = abs(x), True
        elif x > self.max:
            return 0

        while rest > 9:
            if ans >= self.top:
                return 0
            rest, remainder = rest // 10, rest % 10
            ans = ans * 10 + remainder

        if ans > self.top:
            return 0
        if ans == self.top:
            if isNegative and rest > self.negativeRemainder:
                return 0
            elif not isNegative and rest > self.positiveRemainder:
                return 0
        return ans * 10 + rest if not isNegative else ans * -10 - rest


# -1
print(Solution().reverse(-100))

# 0
print(Solution().reverse(1534236469))

# 0
print(Solution().reverse(0))

# 321
print(Solution().reverse(123))

# 21
print(Solution().reverse(120))

# -321
print(Solution().reverse(-123))
