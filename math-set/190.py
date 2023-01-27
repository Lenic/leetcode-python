class Solution:
    def reverseBits(self, n: int) -> int:
        ans: int = 0
        for i in range(32):
            if n == 0:
                break
            ans |= (n & 1) << (31 - i)
            n >>= 1
        return ans


# 964176192
print(Solution().reverseBits(43261596))

# 3221225471
print(Solution().reverseBits(4294967293))
