class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            isBreaked = False
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    isBreaked = True
                    break
            if not isBreaked:
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
