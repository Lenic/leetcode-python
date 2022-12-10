from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left: int = 0
        for i in range(1, len(nums)):
            if nums[left] != nums[i]:
                left += 1
                if left != i:
                    nums[left] = nums[i]
        return left + 1


def polyfill(nums: List[int]):
    k = Solution().removeDuplicates(nums)
    print(k, nums[:k])


# 5 [0,1,2,3,4]
polyfill([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])

# 2 [1, 2]
polyfill([1, 1, 2])
