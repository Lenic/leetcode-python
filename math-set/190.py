class Solution:
    def reverseBits(self, n: int) -> int:
        origin = bin(n)[2:]
        diff = 32 - len(origin)
        mid = "".join(["0"] * diff + [origin])
        return int(mid[::-1], 2)


# 964176192
print(Solution().reverseBits(43261596))

# 3221225471
print(Solution().reverseBits(4294967293))
