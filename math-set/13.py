class Solution:
    def romanToInt(self, s: str) -> int:
        ans, m = 0, len(s) - 1
        for i in range(m, -1, -1):
            val = s[i]
            if val == "I":
                if i < m and (s[i + 1] == "V" or s[i + 1] == "X"):
                    ans -= 1
                else:
                    ans += 1
            elif val == "V":
                ans += 5
            elif val == "X":
                if i < m and (s[i + 1] == "L" or s[i + 1] == "C"):
                    ans -= 10
                else:
                    ans += 10
            elif val == "L":
                ans += 50
            elif val == "C":
                if i < m and (s[i + 1] == "D" or s[i + 1] == "M"):
                    ans -= 100
                else:
                    ans += 100
            elif val == "D":
                ans += 500
            else:
                ans += 1000
        return ans


# 3
print(Solution().romanToInt("III"))

# 4
print(Solution().romanToInt("IV"))

# 9
print(Solution().romanToInt("IX"))

# 58
print(Solution().romanToInt("LVIII"))

# 1994
print(Solution().romanToInt("MCMXCIV"))
