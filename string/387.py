class Solution:
    def firstUniqChar(self, s: str) -> int:
        cache: dict[str, int] = {}
        for i, val in enumerate(s):
            cache[val] = -1 if val in cache else i
        ans: int = len(s)
        for key in cache:
            index = cache[key]
            if index != -1:
                ans = min(ans, index)
        return -1 if ans == len(s) else ans


# 0
print(Solution().firstUniqChar("leetcode"))

# 2
print(Solution().firstUniqChar("loveleetcode"))

# -1
print(Solution().firstUniqChar("aabb"))
