from typing import List


class Solution:
    def binarySearch(self, data: List[int], targetValue: int) -> int:
        left, right = 0, len(data) - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if data[mid] <= targetValue:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()

        index, count = 0, 0
        while index < len(arr1):
            item = arr1[index]
            index += 1

            targetIndex = self.binarySearch(arr2, item)
            if targetIndex == len(arr2):
                if abs(item - arr2[-1]) <= d:
                    continue
            else:
                targetValue = arr2[targetIndex]
                if targetValue <= item:
                    nextIndex = min(targetIndex + 1, len(arr2) - 1)
                    distance = min(abs(item - targetValue), abs(item - arr2[nextIndex]))
                    if distance <= d:
                        continue
                else:
                    nextIndex = max(targetIndex - 1, 0)
                    distance = min(abs(item - arr2[nextIndex]), abs(targetValue - item))
                    if distance <= d:
                        continue
            count += 1
        return count


# 0
print(Solution().findTheDistanceValue([0], [1, 2, 8, 10, 11, 12], 6))

# 1
print(Solution().findTheDistanceValue([2, 1, 100, 3], [-5, -2, 10, -3, 7], 6))

# 2
print(Solution().findTheDistanceValue([1, 4, 2, 3], [-4, -3, 6, 10, 20, 30], 3))

# 2
print(Solution().findTheDistanceValue([4, 5, 8], [10, 9, 1, 8], 2))
