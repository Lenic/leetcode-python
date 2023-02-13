from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        for right in range(k, len(arr)):
            if arr[left] == arr[right] or abs(arr[left] - x) > abs(arr[right] - x):
                left += 1
            else:
                return arr[left:right]
        return arr[left : left + k]


# [10]
print(Solution().findClosestElements(arr=[1, 1, 1, 10, 10, 10], k=1, x=9))

# [3,3,4]
print(Solution().findClosestElements(arr=[0, 0, 1, 2, 3, 3, 4, 7, 7, 8], k=3, x=5))

# [1]
print(Solution().findClosestElements(arr=[1, 2], k=1, x=1))

# [0,1,1,1,2,3,6,7,8]
print(Solution().findClosestElements(arr=[0, 1, 1, 1, 2, 3, 6, 7, 8, 9], k=9, x=4))

# [-2,-1,1,2,3,4,5]
print(Solution().findClosestElements(arr=[-2, -1, 1, 2, 3, 4, 5], k=7, x=3))

# [1,2,3,4]
print(Solution().findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=-1))

# [1,2,3,4]
print(Solution().findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=3))
