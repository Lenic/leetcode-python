from typing import List

import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        data = nums[:k]
        heapq.heapify(data)
        for i in range(k, len(nums)):
            if nums[i] > data[0]:
                heapq.heapreplace(data, nums[i])
        return data[0]


# 4
print(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))

# 5
print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], k=2))
