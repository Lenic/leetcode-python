from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left, ans, cache = 0, 0, set()
        for right, val in enumerate(fruits):
            if len(cache) < 2:
                cache.add(val)
            elif val not in cache:
                cache.clear()
                ans = max(ans, right - left)
                for i in range(right, left - 1, -1):
                    if len(cache) < 2:
                        cache.add(fruits[i])
                    elif len(cache) == 2 and fruits[i] in cache:
                        continue
                    else:
                        left = i + 1
                        break
        ans = max(ans, len(fruits) - left)
        return ans


# 5
print(Solution().totalFruit([0, 1, 6, 6, 4, 4, 6]))

# 5
print(Solution().totalFruit([1, 0, 1, 4, 1, 4, 1, 2, 3]))

# 3
print(Solution().totalFruit([1, 2, 1]))

# 3
print(Solution().totalFruit([0, 1, 2, 2]))

# 4
print(Solution().totalFruit([1, 2, 3, 2, 2]))

# 5
print(Solution().totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
