from typing import List

from collections import deque


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        last = m + n - 1
        while n > 0:
            right = nums2[n - 1]
            if m == 0:
                nums1[last], n = right, n - 1
            else:
                left = nums1[m - 1]
                if left <= right:
                    nums1[last], n = right, n - 1
                else:
                    nums1[last], m = left, m - 1
            last -= 1


def polyfill(nums1: List[int], m: int, nums2: List[int], n: int):
    Solution().merge(nums1, m, nums2, n)
    print(nums1)


# [1]
polyfill(nums1=[0], m=0, nums2=[1], n=1)

# [1,2,2,3,5,6]
polyfill(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)

# [1]
polyfill(nums1=[1], m=1, nums2=[], n=0)
