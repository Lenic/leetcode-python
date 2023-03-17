class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        ans = left = cost = 0
        for right, val in enumerate(s):
            cost += abs(ord(val) - ord(t[right]))
            while cost > maxCost:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            ans = max(ans, right - left + 1)
        return ans


# 1
print(Solution().equalSubstring(s="abcd", t="acde", maxCost=0))

# 1
print(Solution().equalSubstring(s="abcd", t="cdef", maxCost=3))

# 3
print(Solution().equalSubstring(s="abcd", t="bcdf", maxCost=3))
