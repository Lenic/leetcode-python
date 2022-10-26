from typing import List, Optional

from utils import convertArray, TreeNode


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(rest: int, node: Optional[TreeNode]) -> bool:
            if node is None:
                return False
            if node.left is None and node.right is None:
                return rest == node.val
            s = rest - node.val
            return dfs(s, node.left) or dfs(s, node.right)

        return dfs(targetSum, root)


def polyfill(root: List[int | None], targetSum: int):
    print(Solution().hasPathSum(convertArray(root), targetSum))


# False
polyfill(root=[1, 2], targetSum=0)

# False
polyfill(root=[1, 2], targetSum=1)

# True
polyfill(root=[5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], targetSum=22)

# False
polyfill(root=[1, 2, 3], targetSum=5)

# False
polyfill(root=[], targetSum=0)
