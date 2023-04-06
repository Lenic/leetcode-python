from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        prefixSum = [0] * (n + 1)
        for i, val in enumerate(cardPoints):
            prefixSum[i + 1] = prefixSum[i] + val
        ans: int = 0
        if n == k:
            return prefixSum[-1]
        for count in range(-k, k):
            ans = max(ans, (0 if count >= 0 else (prefixSum[n] - prefixSum[n + count])) + prefixSum[k - abs(count)])
        return ans


# 202
print(Solution().maxScore(cardPoints=[1, 79, 80, 1, 1, 1, 200, 1], k=3))

# 1
print(Solution().maxScore(cardPoints=[1, 1000, 1], k=1))

# 55
print(Solution().maxScore(cardPoints=[9, 7, 7, 9, 7, 7, 9], k=7))

# 4
print(Solution().maxScore(cardPoints=[2, 2, 2], k=2))

# 12
print(Solution().maxScore(cardPoints=[1, 2, 3, 4, 5, 6, 1], k=3))
