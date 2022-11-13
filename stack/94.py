from typing import List, Optional

from sys import path
from collections import deque

path.append("../binaryTree")

from utils import convertArray, TreeNode


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans: List[int] = []
        if root is None:
            return ans
        q: deque[TreeNode] = deque([root])
        visited: set[TreeNode] = set()
        while q:
            item = q[-1]
            if item in visited:
                q.pop()
                continue
            if item.left:
                while item.left and item.left not in visited:
                    q.append(item.left)
                    item = item.left
            q.pop()
            visited.add(item)
            ans.append(item.val)
            if item.right:
                q.append(item.right)

        return ans


def polyfill(root: List[int | None]):
    print(Solution().inorderTraversal(convertArray(root)))


# [1,3,2]
polyfill(root=[1, None, 2, 3])

# []
polyfill(root=[])
