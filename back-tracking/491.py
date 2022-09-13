from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res: List[List[int]] = []

        def traverslSegment(begin: int, end: int):
            n = end - begin
            visited = [False] * n

            def dfs(ans: List[int], i: int):
                if i == end:
                    if len(ans) > 1:
                        res.append(ans[:])
                    return

                visitedIndex = i - left
                if i > begin and nums[i] == nums[i - 1] and (not visited[visitedIndex - 1]):
                    dfs(ans, i + 1)
                    return

                visited[visitedIndex] = True
                ans.append(nums[i])
                dfs(ans, i + 1)
                visited[visitedIndex] = False
                ans.pop()
                dfs(ans, i + 1)

            dfs([], begin)

        left: int = 0
        right: int = 1
        while right < len(nums):
            while right < len(nums) and nums[right] >= nums[right - 1]:
                right += 1
            if right - left > 1:
                traverslSegment(left, right)
            left = right
            right += 1

        return res


# too many
print(Solution().findSubsequences([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1, 1, 1]))

# [[4,4]]
print(Solution().findSubsequences([4, 4, 3, 2, 1]))

# [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
print(Solution().findSubsequences([4, 6, 7, 7]))
