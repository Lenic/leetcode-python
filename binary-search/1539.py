from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right, index = 0, len(arr) - 1, -1
        while left <= right:
            mid = left + ((right - left) >> 1)
            val = arr[mid] - mid - 1
            if val < k:
                left = mid + 1
                index = mid
            else:
                right = mid - 1
        return k if index == -1 else k - (arr[index] - index - 1) + arr[index]


# 5
print(Solution().findKthPositive([4, 6, 8], 4))

# 1
print(Solution().findKthPositive([4, 6, 8], 1))

# 13
print(Solution().findKthPositive([2, 3, 4, 7, 11], 8))

# 9
print(Solution().findKthPositive([2, 3, 4, 7, 11], 5))
