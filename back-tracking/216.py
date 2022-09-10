from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res: List[List[int]] = []

        def dfs(ans: List[int], sum: int, val: int, level: int):
            if level == k:
                if sum == n:
                    res.append(ans[:])
                return

            for i in range(val, 10):
                currentSum = sum + i
                if currentSum > n:
                    break

                ans.append(i)
                dfs(ans, currentSum, i + 1, level + 1)
                ans.pop()

        dfs([], 0, 1, 0)
        return res


# [[1,2,3,4,5,6,7,8,9]]
print(Solution().combinationSum3(9, 45))

# [[1,2,4]]
print(Solution().combinationSum3(3, 7))

# [[1,2,6], [1,3,5], [2,3,4]]
print(Solution().combinationSum3(3, 9))
