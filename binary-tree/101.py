from typing import List, Optional

from utils import convertArray, TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        q = [root.left, root.right]
        while q:
            n1, n2 = q.pop(0), q.pop(0)
            if n1 is n2 is None:
                continue
            if n1 is None or n2 is None:
                return False
            if n1.val != n2.val:
                return False
            q.extend([n1.left, n2.right, n1.right, n2.left])
        return True


def polyfill(root: List[int | None]):
    print(Solution().isSymmetric(convertArray(root)))


# True
polyfill(root=[4, -57, -57, None, 67, 67, None, None, -97, -97])

# True
polyfill(root=[1, 2, 2, 3, 4, 4, 3])

# False
polyfill(root=[1, 2, 2, None, 3, None, 3])
