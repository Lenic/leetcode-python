from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counts = [0] * 3
        for val in nums:
            counts[val] += 1
        index = 0
        for i, val in enumerate(counts):
            for j in range(val):
                nums[index], index = i, index + 1


def polyfill(nums: List[int]):
    Solution().sortColors(nums)
    print(nums)


# [1]
polyfill([1])

# [0,1,2]
polyfill([2, 0, 1])

# [0,0,1,1,2,2]
polyfill([2, 0, 2, 1, 1, 0])
