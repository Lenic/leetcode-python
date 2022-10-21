from typing import List, Optional

from utils import convertArray, TreeNode


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans: List[int] = []

        def dfs(node: Optional[TreeNode]):
            if node is None:
                return
            dfs(node.left)
            dfs(node.right)
            ans.append(node.val)

        dfs(root)
        return ans


def polyfill(root: List[int | None]):
    print(Solution().postorderTraversal(convertArray(root)))


# [3,2,1]
polyfill(root=[1, None, 2, 3])

# []
polyfill(root=[])
