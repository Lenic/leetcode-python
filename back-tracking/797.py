from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph) - 1
        res: List[List[int]] = []

        def dfs(ans: List[int], index: int):
            ans.append(index)
            if ans[-1] == n:
                res.append(ans[:])
            else:
                paths = graph[index]
                for val in paths:
                    dfs(ans, val)
            ans.pop()

        dfs([], 0)
        return res


# [[0,2]]
print(Solution().allPathsSourceTarget([[2], [], [1]]))

# [[0,4],[0,3,4],[0,1,3,4],[0,1,4]]
print(Solution().allPathsSourceTarget([[4, 3, 1], [3, 2, 4], [], [4], []]))

# [[0,1,3],[0,2,3]]
print(Solution().allPathsSourceTarget([[1, 2], [3], [3], []]))

# [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
print(Solution().allPathsSourceTarget([[4, 3, 1], [3, 2, 4], [3], [4], []]))
