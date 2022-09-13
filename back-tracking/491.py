from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res: List[List[int]] = []

        def dfs(ans: List[int], index: int):
            if len(ans) > 1:
                res.append(ans[:])

            cache = set()
            for i in range(index, len(nums)):
                item = nums[i]

                if (len(ans) and item < ans[-1]) or (item in cache):
                    continue
                ans.append(item)

                cache.add(item)
                dfs(ans, i + 1)
                ans.pop()

        dfs([], 0)
        return res


# too many
# print(Solution().findSubsequences([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1, 1, 1]))

# [[4,4]]
print(Solution().findSubsequences([4, 4, 3, 2, 1]))

# [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
print(Solution().findSubsequences([4, 6, 7, 7]))
