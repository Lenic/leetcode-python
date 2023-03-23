from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans, target, prefixSum = 0, threshold * k, sum(arr[0 : k - 1])
        for i in range(k - 1, len(arr)):
            prefixSum += arr[i]
            if prefixSum >= target:
                ans += 1
            prefixSum -= arr[i - k + 1]
        return ans


# 5
print(Solution().numOfSubarrays(arr=[1, 1, 1, 1, 1], k=1, threshold=0))

# 6
print(Solution().numOfSubarrays(arr=[11, 13, 17, 23, 29, 31, 7, 5, 2, 3], k=3, threshold=5))

# 3
print(Solution().numOfSubarrays(arr=[2, 2, 2, 2, 5, 5, 5, 8], k=3, threshold=4))
