from typing import List, Optional

from collections import deque

from utils import convertArray, TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans: List[List[int]] = []
        if root is None:
            return ans
        q = deque([root])
        while len(q):
            cur: List[int] = []
            for _ in range(len(q)):
                item = q.popleft()
                cur.append(item.val)
                if item.left:
                    q.append(item.left)
                if item.right:
                    q.append(item.right)
            ans.append(cur)
        return ans


def polyfill(root: List[int | None]):
    print(Solution().levelOrder(convertArray(root)))


# [[3],[9,20],[15,7]]
polyfill(root=[3, 9, 20, None, None, 15, 7])
