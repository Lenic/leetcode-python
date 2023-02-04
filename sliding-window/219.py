from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s: set[int] = set()
        for i, val in enumerate(nums):
            if i > k:
                s.remove(nums[i - k - 1])
            if val in s:
                return True
            s.add(val)
        return False


# false
print(Solution().containsNearbyDuplicate(nums=[1, 2], k=2))

# false
print(Solution().containsNearbyDuplicate(nums=[1], k=1))

# true
print(Solution().containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3))

# true
print(Solution().containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1))

# false
print(Solution().containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2))
