from typing import List

from collections import deque


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        k, mi, ni = m + n - 1, m - 1, n - 1
        while k >= 0 and ni >= 0:
            if mi >= 0:
                if nums1[mi] <= nums2[ni]:
                    nums1[k], ni, k = nums2[ni], ni - 1, k - 1
                else:
                    nums1[k], mi, k = nums1[mi], mi - 1, k - 1
            else:
                nums1[k], ni, k = nums2[ni], ni - 1, k - 1


def polyfill(nums1: List[int], m: int, nums2: List[int], n: int):
    Solution().merge(nums1, m, nums2, n)
    print(nums1)


# [1]
polyfill(nums1=[0], m=0, nums2=[1], n=1)

# [1,2,2,3,5,6]
polyfill(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)

# [1]
polyfill(nums1=[1], m=1, nums2=[], n=0)
