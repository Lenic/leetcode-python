from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        if not k:
            return
        rest = len(nums) - k
        left, right = nums[:rest], nums[rest:]
        for i in range(k):
            nums[i] = right[i]
        for i in range(rest):
            nums[i + k] = left[i]


def polyfill(nums: List[int], k: int):
    Solution().rotate(nums, k)
    print(nums)


# [5,6,7,1,2,3,4]
polyfill(nums=[1, 2, 3, 4, 5, 6, 7], k=3)

# [4,5,6,1,2,3]
polyfill(nums=[1, 2, 3, 4, 5, 6], k=3)

# [5,6,1,2,3,4]
polyfill(nums=[1, 2, 3, 4, 5, 6], k=2)
