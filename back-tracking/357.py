from typing import List


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10

        res, previous = 10, 9
        for i in range(n - 1):
            previous *= 9 - i
            res += previous
        return res


# 91
print(Solution().countNumbersWithUniqueDigits(2))

# 739
print(Solution().countNumbersWithUniqueDigits(3))
