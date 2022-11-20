from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left < right:
            mid = left + ((right - left) >> 1)
            if arr[mid] < arr[mid + 1]:
                left = mid if arr[mid] > arr[right] else (mid + 1)
            else:
                right = mid
        return left


# 1
print(Solution().peakIndexInMountainArray(arr=[3, 9, 8, 6, 4]))

# 1
print(Solution().peakIndexInMountainArray(arr=[0, 1, 0]))

# 1
print(Solution().peakIndexInMountainArray(arr=[0, 2, 1, 0]))

# 1
print(Solution().peakIndexInMountainArray(arr=[0, 10, 5, 2]))

# 2
print(Solution().peakIndexInMountainArray(arr=[3, 4, 5, 1]))

# 2
print(Solution().peakIndexInMountainArray(arr=[24, 69, 100, 99, 79, 78, 67, 36, 26, 19]))
