from typing import List, Optional

from collections import deque

from utils import convertArray, TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans: int = 0
        if root is None:
            return ans
        q = deque([root])
        while len(q):
            ans += 1
            for _ in range(len(q)):
                item = q.popleft()
                if item:
                    if item.left:
                        q.append(item.left)
                    if item.right:
                        q.append(item.right)
        return ans


def polyfill(root: List[int | None]):
    print(Solution().maxDepth(convertArray(root)))


# 3
polyfill([3, 9, 20, None, None, 15, 7])
