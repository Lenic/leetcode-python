from typing import List, Optional

from listNode import convertArrayToTree, TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def traversal(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            leftHeight = traversal(node.left)
            rightHeight = traversal(node.right)
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1
            return max(leftHeight, rightHeight) + 1

        return traversal(root) >= 0


def polyfill(root: list[int | None]):
    print(Solution().isBalanced(convertArrayToTree(root)))


# False
polyfill(root=[1, 2, 2, 3, 3, None, None, 4, 4])

# True
polyfill(root=[3, 9, 20, None, None, 15, 7])
