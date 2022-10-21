from typing import List, Optional

from utils import convertArray, TreeNode


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans: List[int] = []
        if root is None:
            return ans

        def dfs(parent: Optional[TreeNode]):
            if parent is None:
                return
            dfs(parent.left)
            ans.append(parent.val)
            dfs(parent.right)

        dfs(root)
        return ans


def polyfill(root: List[int | None]):
    print(Solution().inorderTraversal(convertArray(root)))


# [1,3,2]
polyfill(root=[1, None, 2, 3])

# []
polyfill(root=[])
