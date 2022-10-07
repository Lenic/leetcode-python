from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            maxLeft, minRight = max(0, mid - 1), min(mid + 1, len(arr) - 1)
            if arr[maxLeft] <= arr[mid] >= arr[minRight]:
                return mid
            elif arr[maxLeft] > arr[mid]:
                right = mid
            else:
                left = mid + 1
        return -1


# 0
print(Solution().peakIndexInMountainArray([3, 2, 1, 0]))

# 3
print(Solution().peakIndexInMountainArray([0, 1, 2, 3]))

# 1
print(Solution().peakIndexInMountainArray([0, 2, 1, 0]))

# 1
print(Solution().peakIndexInMountainArray([0, 10, 5, 2]))

# 1
print(Solution().peakIndexInMountainArray([0, 1, 0]))
