class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        for i in range(n):
            val = 3**i
            if val == n:
                return True
            elif val > n:
                return False
        return False


# True
print(Solution().isPowerOfThree(27))

# False
print(Solution().isPowerOfThree(-1))

# True
print(Solution().isPowerOfThree(1))

# False
print(Solution().isPowerOfThree(0))

# True
print(Solution().isPowerOfThree(9))

# False
print(Solution().isPowerOfThree(45))
