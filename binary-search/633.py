class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        maxValue = int(c**0.5)
        for i in range(c + 1):
            if i**2 > c:
                break

            left, right = i, maxValue
            while left <= right:
                mid = left + ((right - left) >> 1)
                val = i**2 + mid**2
                if val < c:
                    left = mid + 1
                elif val > c:
                    right = mid - 1
                else:
                    return True
        return False


# False
print(Solution().judgeSquareSum(999999999))

# True
print(Solution().judgeSquareSum(0))

# True
print(Solution().judgeSquareSum(4))

# True
print(Solution().judgeSquareSum(5))

# False
print(Solution().judgeSquareSum(3))
