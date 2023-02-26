from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        ans1 = ans2 = 1
        left1 = left2 = 0
        for right in range(1, len(arr)):
            odd = right % 2 == 1
            if (odd and arr[right - 1] > arr[right]) or (not odd and arr[right - 1] < arr[right]):
                ans1 = max(ans1, right - left1 + 1)
            else:
                left1 = right
            if (odd and arr[right - 1] < arr[right]) or (not odd and arr[right - 1] > arr[right]):
                ans2 = max(ans2, right - left2 + 1)
            else:
                left2 = right
        return max(ans1, ans2)


# 5
print(Solution().maxTurbulenceSize([37, 199, 60, 296, 257, 248, 115, 31, 273, 176]))

# 5
print(Solution().maxTurbulenceSize([0, 1, 1, 0, 1, 0, 1, 1, 0, 0]))

# 5
print(Solution().maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]))

# 2
print(Solution().maxTurbulenceSize([4, 8, 12, 16]))

# 1
print(Solution().maxTurbulenceSize([100]))
