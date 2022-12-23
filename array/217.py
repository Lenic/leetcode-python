from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cache: set[int] = set()
        for val in nums:
            if val in cache:
                return True
            cache.add(val)
        return False


# true
print(Solution().containsDuplicate([1, 2, 3, 1]))
