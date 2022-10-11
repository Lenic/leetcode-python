from typing import List

import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda x: x[0])

        pq: List[tuple[int, List[int]]] = [(intervals[0][1], intervals[0])]
        for i in range(1, n):
            item = intervals[i]
            top = pq[0][1]
            if item[0] >= top[1]:
                heapq.heapreplace(pq, (item[1], item))
            else:
                heapq.heappush(pq, (item[1], item))
        return len(pq)


# 2
print(Solution().minMeetingRooms([[5, 8], [6, 8]]))

# 2
print(Solution().minMeetingRooms([[0, 30], [15, 20], [5, 10]]))

# 1
print(Solution().minMeetingRooms([[7, 10], [2, 4]]))
