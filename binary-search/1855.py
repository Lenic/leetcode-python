from typing import List


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        res: int = 0
        for i in range(len(nums1)):
            item = nums1[i]
            left, right = i, len(nums2) - 1
            while left <= right:
                mid = left + ((right - left) >> 1)
                if nums2[mid] >= item:
                    left = mid + 1
                else:
                    right = mid - 1
            res = max(res, right - i)
        return res


# 9
print(
    Solution().maxDistance(
        [9819, 9508, 7398, 7347, 6337, 5756, 5493, 5446, 5123, 3215, 1597, 774, 368, 313],
        [9933, 9813, 9770, 9697, 9514, 9490, 9441, 9439, 8939, 8754, 8665, 8560],
    )
)

# 1
print(Solution().maxDistance([2, 2, 2], [10, 10, 1]))

# 2
print(Solution().maxDistance([55, 30, 5, 4, 2], [100, 20, 10, 10, 5]))
