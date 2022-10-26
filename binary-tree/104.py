from typing import List, Optional

from utils import convertArray, TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(parent: Optional[TreeNode]) -> int:
            if parent is None:
                return 0
            return max(dfs(parent.left), dfs(parent.right)) + 1

        return dfs(root)


def polyfill(root: List[int | None]):
    print(Solution().maxDepth(convertArray(root)))


# 3
polyfill([3, 9, 20, None, None, 15, 7])
