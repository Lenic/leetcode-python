class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        ans, initialValue = 0, ord("a")
        for i in range(1, min(27, len(s) + 1)):
            total = less = l = r = 0
            cache = [0] * 26
            while r < len(s):
                rightIndex = ord(s[r]) - initialValue
                cache[rightIndex] += 1
                if cache[rightIndex] == 1:
                    total += 1
                    less += 1
                if cache[rightIndex] == k:
                    less -= 1
                while total > i:
                    leftIndex = ord(s[l]) - initialValue
                    cache[leftIndex] -= 1
                    if cache[leftIndex] == k - 1:
                        less += 1
                    if cache[leftIndex] == 0:
                        total -= 1
                        less -= 1
                    l += 1
                if less == 0:
                    ans = max(ans, r - l + 1)
                r += 1
        return ans


# 3
print(Solution().longestSubstring(s="bbaaacbd", k=3))

# 5
print(Solution().longestSubstring(s="ababbc", k=2))

# 3
print(Solution().longestSubstring(s="aaabb", k=3))
