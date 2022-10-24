from typing import List, Optional

from utils import convertArray, TreeNode


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans: List[int] = []
        if root is None:
            return ans
        cur = root
        while cur:
            if cur.left is None:
                ans.append(cur.val)
                cur = cur.right
            else:
                mostRight = cur.left
                while mostRight.right is not None and mostRight.right is not cur:
                    mostRight = mostRight.right
                if mostRight.right is None:
                    mostRight.right = cur
                    ans.append(cur.val)
                    cur = cur.left
                if mostRight.right is cur:
                    mostRight.right = None
                    cur = cur.right
        return ans


def polyfill(root: List[int | None]):
    print(Solution().preorderTraversal(convertArray(root)))


# [1,2,3]
polyfill(root=[1, None, 2, 3])

# []
polyfill(root=[])
