from typing import List


class Solution:
    def binarySearch(self, data: List[int], targetValue: int, left: int, right: int) -> int:
        ans = left
        while left <= right and left < len(data):
            mid = left + ((right - left) >> 1)
            if data[mid] < targetValue:
                left = mid + 1
            elif data[mid] >= targetValue:
                right = mid - 1
                ans = mid
        return ans

    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        n = len(arr)

        index = self.binarySearch(arr, 0, 0, n - 1)
        if index > 1:
            for i in range(index, 0, -1):
                targetValue = arr[i] * 2
                j = self.binarySearch(arr, targetValue, 0, i - 1)
                if arr[j] == targetValue:
                    return True
        if index < n - 1:
            for i in range(index, n):
                targetValue = arr[i] * 2
                j = self.binarySearch(arr, targetValue, i + 1, n - 1)
                if j < n and arr[j] == targetValue:
                    return True
        return False


# True
print(Solution().checkIfExist([0, 0]))

# False
print(Solution().checkIfExist([-10, -12, -21, -8]))

# True
print(Solution().checkIfExist([-10, 12, -20, -8, 15]))

# True
print(Solution().checkIfExist([10, 2, 5, 3]))

# True
print(Solution().checkIfExist([7, 1, 14, 11]))

# False
print(Solution().checkIfExist([3, 1, 7, 11]))
