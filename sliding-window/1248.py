from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        cnt = [0] * (len(nums) + 1)
        cnt[0] = 1
        odd, ans = 0, 0
        for num in nums:
            if num % 2 == 1:
                odd += 1
            if odd >= k:
                ans += cnt[odd - k]
            cnt[odd] += 1
        return ans


# 5
print(Solution().numberOfSubarrays(nums=[1, 1, 1, 1, 1], k=1))

# 16
print(Solution().numberOfSubarrays(nums=[2, 2, 2, 1, 2, 2, 1, 2, 2, 2], k=2))

# 0
print(Solution().numberOfSubarrays(nums=[2, 4, 6], k=1))

# 2
print(Solution().numberOfSubarrays(nums=[1, 1, 2, 1, 1], k=3))
