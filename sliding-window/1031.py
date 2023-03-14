from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n, maxIndex = len(nums), len(nums) - 1

        def getSubArrayMaxSum(left: int, right: int, count: int) -> int:
            ans = 0
            if right - left + 1 < count:
                return ans
            l, r = left, left + count - 1
            s = sum(nums[l:r])
            while r <= right:
                s += nums[r]
                ans = max(ans, s)
                s -= nums[l]
                l += 1
                r += 1
            return ans

        ans = 0
        l1, r1 = 0, firstLen - 1
        s = sum(nums[l1:r1])
        while r1 < n:
            s += nums[r1]
            r1 += 1
            other = max(getSubArrayMaxSum(r1, maxIndex, secondLen), getSubArrayMaxSum(0, l1 - 1, secondLen))
            ans = max(ans, s + other)
            s -= nums[l1]
            l1 += 1
        return ans


# 20
print(Solution().maxSumTwoNoOverlap(nums=[0, 6, 5, 2, 2, 5, 1, 9, 4], firstLen=1, secondLen=2))

# 108
print(Solution().maxSumTwoNoOverlap(nums=[8, 20, 6, 2, 20, 17, 6, 3, 20, 8, 12], firstLen=5, secondLen=4))
