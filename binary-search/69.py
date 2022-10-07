class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        while left <= right:
            mid = left + ((right - left) >> 1)
            val = mid * mid
            if val > x:
                right = mid - 1
            else:
                left = mid + 1
        return right


# 0
print(Solution().mySqrt(0))

# 2
print(Solution().mySqrt(8))

# 2
print(Solution().mySqrt(4))

# 4
print(Solution().mySqrt(18))
