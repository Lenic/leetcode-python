from typing import List, Optional

from queue import Queue

from utils import convertArray, TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        q: Queue[TreeNode | None] = Queue()
        q.put_nowait(root.left)
        q.put_nowait(root.right)
        while not q.empty():
            n1, n2 = q.get_nowait(), q.get_nowait()
            if n1 is None and n2 is None:
                continue
            if n1 is None or n2 is None:
                return False
            if n1.val != n2.val:
                return False
            q.put_nowait(n1.left)
            q.put_nowait(n2.right)
            q.put_nowait(n1.right)
            q.put_nowait(n2.left)
        return True


def polyfill(root: List[int | None]):
    print(Solution().isSymmetric(convertArray(root)))


# True
polyfill(root=[4, -57, -57, None, 67, 67, None, None, -97, -97])

# True
polyfill(root=[1, 2, 2, 3, 4, 4, 3])

# False
polyfill(root=[1, 2, 2, None, 3, None, 3])
