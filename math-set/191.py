class Solution:
    def hammingWeight(self, n: int) -> int:
        ans, s = 0, bin(n)
        for val in s:
            if val == "1":
                ans += 1
        return ans


# 3
print(Solution().hammingWeight(0b00000000000000000000000000001011))
