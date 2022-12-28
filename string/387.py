class Solution:
    def firstUniqChar(self, s: str) -> int:
        cache: dict[str, tuple[int, int]] = {}
        for i, val in enumerate(s):
            item = cache.get(val)
            if item is None:
                cache[val] = (i, 1)
            else:
                cache[val] = (item[0], item[1] + 1)
        index: int = len(s)
        for key in cache:
            if cache[key][1] == 1:
                index = min(index, cache[key][0])
        return -1 if index == len(s) else index


# 0
print(Solution().firstUniqChar("leetcode"))

# 2
print(Solution().firstUniqChar("loveleetcode"))

# -1
print(Solution().firstUniqChar("aabb"))
