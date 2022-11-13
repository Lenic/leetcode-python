from typing import List, Optional
from typing_extensions import Self

from collections import deque

# '../binary-tree/utils.py


class TreeNode:
    def __init__(self, val: int = 0, left: Self | None = None, right: Self | None = None):
        self.val = val
        self.left = left
        self.right = right


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


def convertArray(data: List[int | None]) -> Optional[TreeNode]:
    if not data:
        return None
    item = data[0]
    if item is None:
        return None

    root = TreeNode(item)
    q: deque[TreeNode | None] = deque([])
    q.append(root)

    i, n = 1, len(data)
    while q and i < n:
        item = q.popleft()
        if item is not None:
            if i < n:
                leftValue = data[i]
                if leftValue is not None:
                    item.left = TreeNode(leftValue)
                    q.append(item.left)
            if i + 1 < n:
                rightValue = data[i + 1]
                if rightValue is not None:
                    item.right = TreeNode(rightValue)
                    q.append(item.right)
            i += 2
    return root


def polyfill(root: List[int | None]):
    print(Solution().inorderTraversal(convertArray(root)))


# [1,3,2]
polyfill(root=[1, None, 2, 3])

# []
polyfill(root=[])
