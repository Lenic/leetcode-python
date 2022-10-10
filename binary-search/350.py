from typing import List


class Solution:
    def binarySearch(self, data: List[int], targetValue: int, left: int) -> int:
        right = len(data) - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if data[mid] < targetValue:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        shortArr, longArr = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)

        index: int = 0
        res: List[int] = []
        for i in range(len(shortArr)):
            nextIndex = self.binarySearch(longArr, shortArr[i], index)
            if nextIndex < len(longArr) and longArr[nextIndex] == shortArr[i]:
                res.append(shortArr[i])
                index = nextIndex + 1
        return res


# [1]
print(Solution().intersect([1, 3, 8, 9, 3], [1, 0]))

# [4,6]
print(Solution().intersect([4, 7, 9, 7, 6, 7], [5, 0, 0, 6, 1, 6, 2, 2, 4]))

# [1]
print(Solution().intersect([1, 2], [1, 1]))

# [4, 9]
print(Solution().intersect([4, 9, 5], [9, 4, 9, 8, 4]))

# [2,2]
print(Solution().intersect([1, 2, 2, 1], [2, 2]))
