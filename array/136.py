from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        i, n = 0, len(nums)
        while i < n:
            j = i + 1
            while j < n:
                if nums[i] == nums[j]:
                    i += 1
                    while i < j and nums[i] != nums[j]:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                    break
                j += 1
            if j == n:
                return nums[i]
            i += 1
        return -1


# 1
print(Solution().singleNumber([1]))

# 4
print(Solution().singleNumber([4, 1, 2, 1, 2]))

# 1
print(Solution().singleNumber([2, 2, 1]))
