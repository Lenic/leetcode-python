class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        if m < n:
            return -1

        next = [0] * n
        next[0] = -1
        # build next
        for i in range(1, n - 1):
            right = i + 1
            while right > 1:
                right -= 1
                j, k = 0, right
                while k <= i:
                    if needle[j] != needle[k]:
                        break
                    j, k = j + 1, k + 1
                if k > i:
                    next[i + 1] = j

        i, j, count = 0, 0, m - n + 1
        while i < count:
            while j < n:
                if haystack[i + j] != needle[j]:
                    break
                j += 1
            if j == n:
                return i
            else:
                i, j = i + j - next[j], i + j
                j = max(0, j - i)

        return -1


# -1
print(Solution().strStr(haystack="mississippi", needle="issipi"))

# 15
print(Solution().strStr(haystack="BBC ABCDAB ABCDABCDABDE", needle="ABCDABD"))

# 2
print(Solution().strStr(haystack="abc", needle="c"))

# 0
print(Solution().strStr(haystack="a", needle="a"))

# 0
print(Solution().strStr(haystack="sadbutsad", needle="sad"))

# -1
print(Solution().strStr(haystack="leetcode", needle="leeto"))
