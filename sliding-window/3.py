class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, ans, cache = 0, 0, set()
        for i, val in enumerate(s):
            if val in cache:
                ans = max(ans, len(cache))
                for j in range(left, i):
                    if s[j] == val:
                        left = j + 1
                        break
                    else:
                        cache.remove(s[j])
            else:
                cache.add(val)
        ans = max(ans, len(cache))
        return ans


# 1
print(Solution().lengthOfLongestSubstring(" "))

# 3
print(Solution().lengthOfLongestSubstring("pwwkew"))

# 1
print(Solution().lengthOfLongestSubstring("bbbbb"))

# 3
print(Solution().lengthOfLongestSubstring("abcabcbb"))
