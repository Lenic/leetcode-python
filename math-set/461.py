class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return sum(int(item) for item in bin(x ^ y)[2:])


# 2
print(Solution().hammingDistance(x=1, y=4))
