class Solution:
    minValue = ord("0")

    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        converted = " " + s
        dp = [1] + [0] * len(s)
        for i in range(1, len(converted)):
            current = ord(converted[i]) - self.minValue
            if 1 <= current <= 9:
                dp[i] = dp[i - 1]

            double = (ord(converted[i - 1]) - self.minValue) * 10 + current
            if 10 <= double <= 26:
                dp[i] += dp[i - 2]

        return dp[-1]


# 5
print(Solution().numDecodings("1123"))

# 1
print(Solution().numDecodings("27"))

# 1
print(Solution().numDecodings("10"))

# 1
print(Solution().numDecodings("110"))

# 1
print(Solution().numDecodings("810"))

# 2
print(Solution().numDecodings("11106"))

# 2
print(Solution().numDecodings("12"))

# 3
print(Solution().numDecodings("226"))

# 0
print(Solution().numDecodings("0"))
