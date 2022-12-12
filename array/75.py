from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i, lt, gt = 0, -1, len(nums)
        while i < gt:
            if nums[i] == 0:
                lt += 1
                nums[lt], nums[i] = nums[i], nums[lt]
                i += 1
            elif nums[i] == 2:
                gt -= 1
                nums[gt], nums[i] = nums[i], nums[gt]
            else:
                i += 1


def polyfill(nums: List[int]):
    Solution().sortColors(nums)
    print(nums)


# [1]
polyfill([1])

# [0,1,2]
polyfill([2, 0, 1])

# [0,0,1,1,2,2]
polyfill([2, 0, 2, 1, 1, 0])
