class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n = n // 3
        return True if n == 1 else False


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
