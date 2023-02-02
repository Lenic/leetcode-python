from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        cache: dict[int, list[int]] = {}
        for i, val in enumerate(nums):
            if val in cache:
                if any(abs(i - j) <= k for j in cache[val]):
                    return True
                cache[val].append(i)
            else:
                cache[val] = [i]

        return False


# true
print(Solution().containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3))

# true
print(Solution().containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1))

# false
print(Solution().containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2))
