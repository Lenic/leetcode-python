from typing import List, Optional

from collections import deque

from utils import convertArray, TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        left, right = deque([root.left]), deque([root.right])
        while len(left):
            if len(right) != len(left):
                return False
            for _ in range(len(left)):
                x = left.popleft()
                y = right.popleft()
                if x is None and y is None:
                    continue
                if x is not None and y is not None and x.val == y.val:
                    left.append(x.left)
                    left.append(x.right)
                    right.append(y.right)
                    right.append(y.left)
                else:
                    return False
        return True


def polyfill(root: List[int | None]):
    print(Solution().isSymmetric(convertArray(root)))


# False
polyfill(root=[1, 2, 2, None, 3, None, 3])

# True
polyfill(root=[4, -57, -57, None, 67, 67, None, None, -97, -97])

# True
polyfill(root=[1, 2, 2, 3, 4, 4, 3])
