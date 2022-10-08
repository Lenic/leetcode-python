from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n - 1):
            left, right = i + 1, n - 1
            while left <= right:
                rest = target - numbers[i]
                if numbers[left] <= rest <= numbers[right]:
                    mid = left + ((right - left) >> 1)
                    if numbers[mid] < rest:
                        left = mid + 1
                    elif numbers[mid] > rest:
                        right = mid - 1
                    else:
                        return [i + 1, mid + 1]
                else:
                    break
        return [-1, -1]


# [1,2]
print(Solution().twoSum([-1, 0], -1))

# [2,3]
print(Solution().twoSum([2, 3, 4], 7))

# [1,3]
print(Solution().twoSum([2, 3, 4], 6))

# [1,2]
print(Solution().twoSum([2, 7, 11, 15], 9))
