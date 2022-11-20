from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        left, right = intervals[0]
        ans: List[List[int]] = []
        for i in range(1, len(intervals)):
            begin, end = intervals[i]
            if left <= begin <= right:
                right = max(right, end)
            elif right < begin:
                ans.append([left, right])
                left, right = begin, end
        ans.append([left, right])
        return ans


# [[1,6],[8,10],[15,18]]
print(Solution().merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))

# [[1,5]]
print(Solution().merge(intervals=[[1, 4], [4, 5]]))
