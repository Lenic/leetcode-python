from typing import List, Optional
from typing_extensions import Self

from queue import Queue


class TreeNode:
    def __init__(self, val: int = 0, left: Self | None = None, right: Self | None = None):
        self.val = val
        self.left = left
        self.right = right


def convertArray(data: List[int | None]) -> Optional[TreeNode]:
    if not data:
        return None
    item = data[0]
    if item is None:
        return None

    root = TreeNode(item)
    q: Queue[TreeNode | None] = Queue()
    q.put(root)

    i, n = 1, len(data)
    while not q.empty() and i < n:
        item = q.get()
        if item is not None:
            if i < n:
                leftValue = data[i]
                if leftValue is not None:
                    item.left = TreeNode(leftValue)
                    q.put(item.left)
            if i + 1 < n:
                rightValue = data[i + 1]
                if rightValue is not None:
                    item.right = TreeNode(rightValue)
                    q.put(item.right)
            i += 2
    return root


def convertTree(head: Optional[TreeNode]) -> List[int | None]:
    ans: List[int | None] = []
    cur, next = [head], []
    while cur:
        values, hasValue = [], False
        for node in cur:
            if node is None:
                values.append(None)
            else:
                hasValue = True
                values.append(node.val)
                next.extend([node.left, node.right])
        cur, next = next, []
        if hasValue:
            ans.extend(values)
    while ans and ans[-1] is None:
        ans.pop()
    return ans
