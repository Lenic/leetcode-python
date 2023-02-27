from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = count = left = right = 0
        while right < len(nums):
            if count == k:
                ans = max(ans, right - left)
            if nums[right] == 0:
                count += 1
            while count > k:
                while left <= right:
                    if nums[left] == 0:
                        left += 1
                        count -= 1
                        break
                    else:
                        left += 1
            right += 1
        return max(ans, right - left)


# 4
print(Solution().longestOnes(nums=[0, 0, 0, 1], k=4))

# 6
print(Solution().longestOnes(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2))

# 10
print(Solution().longestOnes(nums=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=3))
