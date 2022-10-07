# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:


class PredefinedValue:
    targetValue: int = -1


def guess(num: int) -> int:
    return -1 if PredefinedValue.targetValue < num else 1 if PredefinedValue.targetValue > num else 0


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = left + ((right - left) >> 1)
            val = guess(mid)
            if val < 0:
                right = mid - 1
            elif val > 0:
                left = mid + 1
            else:
                return mid
        return -1


def polyfill(n: int, k: int):
    PredefinedValue.targetValue = k
    print(Solution().guessNumber(n))


# 1
polyfill(1, 1)

# 6
polyfill(10, 6)
