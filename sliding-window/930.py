from typing import List
from collections import defaultdict


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans, s, cnt = 0, 0, defaultdict(int)
        for val in nums:
            cnt[s] += 1
            s += val
            ans += cnt[s - goal]
        return ans


# 4
print(Solution().numSubarraysWithSum(nums=[1, 0, 1, 0, 1], goal=2))

# 15
print(Solution().numSubarraysWithSum(nums=[0, 0, 0, 0, 0], goal=0))
