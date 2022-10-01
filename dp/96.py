class Solution:
    def numTrees(self, n: int) -> int:
        data = [1] * 2 + [0] * (n - 1)
        for i in range(2, len(data)):
            for j in range(i):
                data[i] += data[j] * data[i - j - 1]
        return data[-1]


# 2
print(Solution().numTrees(1))

# 5
print(Solution().numTrees(3))

# 14
print(Solution().numTrees(4))
