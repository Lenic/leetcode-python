from typing import List, Optional

from sys import maxsize

from utils import convertArray, TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node: Optional[TreeNode], lower: int, upper: int) -> bool:
            if node is None:
                return True
            if not (lower < node.val < upper):
                return False
            if not isValid(node.left, lower, node.val) or not isValid(node.right, node.val, upper):
                return False
            return True

        return isValid(root, -maxsize, maxsize)


def polyfill(root: List[int | None]):
    print(Solution().isValidBST(convertArray(root)))


# false
polyfill([5, 4, 6, None, None, 3, 7])

# true
polyfill([2, 1, 3])

# false
polyfill([5, 1, 4, None, None, 3, 6])
