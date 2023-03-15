from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        cur = ans = sum(customers[i] for i in range(minutes) if grumpy[i] == 1)
        for right in range(minutes, len(customers)):
            cur += customers[right] if grumpy[right] == 1 else 0
            left = right - minutes
            cur -= customers[left] if grumpy[left] == 1 else 0
            ans = max(ans, cur)
        return ans + sum(customers[i] for i in range(len(customers)) if grumpy[i] == 0)


# 29
print(Solution().maxSatisfied(customers=[7, 8, 8, 6], grumpy=[0, 1, 0, 1], minutes=3))

# 1
print(Solution().maxSatisfied(customers=[1], grumpy=[0], minutes=1))

# 16
print(Solution().maxSatisfied(customers=[1, 0, 1, 2, 1, 1, 7, 5], grumpy=[0, 1, 0, 1, 0, 1, 0, 1], minutes=3))
