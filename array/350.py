from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1, n2 = len(nums1), len(nums2)
        s, l = nums1 if n1 <= n2 else nums2, nums2 if n1 <= n2 else nums1
        map: dict[int, int] = {}
        for val in l:
            if val not in map:
                map[val] = 1
            else:
                map[val] += 1
        ans: List[int] = []
        for val in s:
            if val in map and map[val] > 0:
                ans.append(val)
                map[val] -= 1
        return ans


# [2,2]
print(Solution().intersect(nums1=[1, 2, 2, 1], nums2=[2, 2]))

# [4,9]
print(Solution().intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))
