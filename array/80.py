from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, count = 0, 1
        for i in range(1, len(nums)):
            if nums[left] == nums[i]:
                if count < 2:
                    count += 1
                else:
                    continue
            else:
                count = 1
            left += 1
            nums[left] = nums[i]
        return left + 1


def polyfill(nums: List[int]):
    k = Solution().removeDuplicates(nums)
    print(k, nums[:k])


# 7, nums = [0,0,1,1,2,3,3]
polyfill([0, 0, 1, 1, 1, 1, 2, 3, 3])

# 5, nums = [1,1,2,2,3]
polyfill([1, 1, 1, 2, 2, 3])
