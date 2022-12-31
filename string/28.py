class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        if m < n:
            return -1
        for i in range(m - n + 1):
            j = 0
            while j < n:
                if haystack[i + j] != needle[j]:
                    break
                j += 1
            if j == n:
                return i
        return -1


# 2
print(Solution().strStr(haystack="abc", needle="c"))

# 0
print(Solution().strStr(haystack="a", needle="a"))

# 0
print(Solution().strStr(haystack="sadbutsad", needle="sad"))

# -1
print(Solution().strStr(haystack="leetcode", needle="leeto"))
