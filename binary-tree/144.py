from typing import List, Optional

from utils import convertArray, TreeNode


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans: List[int] = []
        if root is None:
            return ans

        def dfs(parent: Optional[TreeNode]):
            if parent is None:
                return

            ans.append(parent.val)
            dfs(parent.left)
            dfs(parent.right)

        dfs(root)
        return ans


def polyfill(root: List[int | None]):
    print(Solution().preorderTraversal(convertArray(root)))


# [1,2,3]
polyfill(root=[1, None, 2, 3])

# []
polyfill(root=[])
