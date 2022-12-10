from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = -1
        for i, val in enumerate(nums):
            if val == 0:
                left = i
                break
        if left == -1:
            return
        count = 1
        for i in range(left + 1, len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                nums[left], left = nums[i], left + 1
        for i in range(len(nums) - count, len(nums)):
            nums[i] = 0


def polyfill(nums: List[int]):
    Solution().moveZeroes(nums)
    print(nums)


# [-58305,-22022,-76070,42820,48119,95708,-91393,60044,-34562,-88974,0,0,0,0,0,0,0,0]
polyfill([-58305, -22022, 0, 0, 0, 0, 0, -76070, 42820, 48119, 0, 95708, -91393, 60044, 0, -34562, 0, -88974])

# [1,0,0]
polyfill([0, 1, 0])

# [1,1,1,0,0,0,0,0,0]
polyfill([0, 0, 0, 0, 0, 0, 1, 1, 1])

# [1,3,12,0,0]
polyfill([0, 1, 0, 3, 12])

# [0]
polyfill([0])
