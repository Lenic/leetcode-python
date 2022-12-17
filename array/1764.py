from typing import List


class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        totalCount = sum(len(val) for val in groups)
        if totalCount > len(nums):
            return False

        index, i, m, count = 0, 0, len(nums) - totalCount, 0
        while i <= m and index < len(groups):
            item, matched = groups[index], True
            for j, val in enumerate(item):
                if val != nums[i + count + j]:
                    matched = False
                    break
            if matched:
                index += 1
                count += len(item)
            else:
                i += 1
        return totalCount == count


# true
#           1, -1, -1, 3, -2, 0
# 1, -1, 0, 1, -1, -1, 3, -2, 0
print(Solution().canChoose(groups=[[1, -1, -1], [3, -2, 0]], nums=[1, -1, 0, 1, -1, -1, 3, -2, 0]))
