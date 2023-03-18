from collections import Counter


class Solution:
    arr = ["Q", "W", "E", "R"]

    def balancedString(self, s: str) -> int:
        target, counter = len(s) // 4, Counter(s)

        mapper, total = {}, 0
        for val in self.arr:
            count = counter.get(val, 0)
            if count > target:
                mapper[val] = count - target
                total += mapper[val]

        if total == 0:
            return 0

        ans, left = len(s), 0
        for right, val in enumerate(s):
            if val in mapper:
                mapper[val] -= 1
                total -= 1
            while total <= 0 and left <= right and all(val <= 0 for val in mapper.values()):
                ans = min(ans, right - left + 1)
                if s[left] in mapper:
                    mapper[s[left]] += 1
                    total += 1
                left += 1
        return ans


# 3
print(Solution().balancedString("WQWRQQQW"))

# 4
print(Solution().balancedString("WWEQERQWQWWRWWERQWEQ"))

# 0
print(Solution().balancedString("QWER"))

# 1
print(Solution().balancedString("QQWE"))

# 2
print(Solution().balancedString("QQQW"))

# 3
print(Solution().balancedString("QQQQ"))
