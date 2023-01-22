class Solution:
    def countPrimes(self, n: int) -> int:
        cache = [True] * n
        ans: int = 0
        for i in range(2, n):
            if cache[i]:
                ans += 1
                for j in range(i, n):
                    val = i * j
                    if val < n:
                        cache[val] = False
                    else:
                        break
        return ans


# 4
print(Solution().countPrimes(10))

# 0
print(Solution().countPrimes(0))

# 0
print(Solution().countPrimes(1))

# 0
print(Solution().countPrimes(2))
