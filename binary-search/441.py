class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right, row = 1, n, 0
        while left <= right:
            mid = left + ((right - left) >> 1)
            val = (mid + 1) * mid // 2

            if val < n:
                left = mid + 1
                row = mid
            elif val > n:
                right = mid - 1
            else:
                return mid
        return row


# 1
print(Solution().arrangeCoins(1))

# 3
print(Solution().arrangeCoins(6))

# 3
print(Solution().arrangeCoins(8))

# 2
print(Solution().arrangeCoins(5))
