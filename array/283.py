from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1


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
