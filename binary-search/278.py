# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class PredefinedValue:
    version: int = -1


def isBadVersion(version: int) -> bool:
    return version >= PredefinedValue.version


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = left + ((right - left) >> 1)
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left


def polyfill(n: int, k: int):
    PredefinedValue.version = k
    print(Solution().firstBadVersion(n))


# 1
polyfill(1, 1)

# 4
polyfill(5, 4)
