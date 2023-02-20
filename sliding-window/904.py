from typing import List

from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left, ans, cache = 0, 0, defaultdict(int)
        for right, val in enumerate(fruits):
            cache[val] += 1
            while len(cache) > 2:
                cache[fruits[left]] -= 1
                if cache[fruits[left]] == 0:
                    cache.pop(fruits[left])
                left += 1
            ans = max(ans, right - left + 1)
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
