class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num

        while left <= right:
            mid = left + ((right - left) >> 1)
            val = mid**2
            if val > num:
                right = mid - 1
            elif val < num:
                left = mid + 1
            else:
                return True
        return False


# False
print(Solution().isPerfectSquare(14))

# True
print(Solution().isPerfectSquare(1))

# True
print(Solution().isPerfectSquare(16))
