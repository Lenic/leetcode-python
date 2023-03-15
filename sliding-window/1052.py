from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        preset = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                preset += customers[i]

        ans = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                ans += customers[i]

        left, cur = 0, ans
        for right in range(minutes, len(customers)):
            if grumpy[right] == 1:
                cur += customers[right]
            if grumpy[left] == 1:
                cur -= customers[left]
            left += 1
            ans = max(ans, cur)
        return ans + preset


# 29
print(Solution().maxSatisfied(customers=[7, 8, 8, 6], grumpy=[0, 1, 0, 1], minutes=3))

# 1
print(Solution().maxSatisfied(customers=[1], grumpy=[0], minutes=1))

# 16
print(Solution().maxSatisfied(customers=[1, 0, 1, 2, 1, 1, 7, 5], grumpy=[0, 1, 0, 1, 0, 1, 0, 1], minutes=3))
