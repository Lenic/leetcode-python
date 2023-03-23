from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = threshold * k

        prefixSum = [0] * (len(arr) + 1)
        for i, val in enumerate(arr):
            prefixSum[i + 1] = prefixSum[i] + val

        ans: int = 0
        for i in range(len(arr) - k + 1):
            val = prefixSum[i + k] - prefixSum[i]
            if val >= target:
                ans += 1

        return ans


# 6
print(Solution().numOfSubarrays(arr=[11, 13, 17, 23, 29, 31, 7, 5, 2, 3], k=3, threshold=5))

# 3
print(Solution().numOfSubarrays(arr=[2, 2, 2, 2, 5, 5, 5, 8], k=3, threshold=4))
