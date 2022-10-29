from typing import Optional, List
from typing_extensions import Self

from collections import deque


class Node:
    def __init__(self, val: int = 0, left: Self | None = None, right: Self | None = None, next: Self | None = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        q = deque([root])
        prev: Node | None = None
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node is None:
                    continue
                if prev is not None:
                    prev.next = node
                if node.left:
                    node.left.next = node.right
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                prev = node
            prev = None
        return root


def polyfill(root: List[int | None]):
    index, head = 1, Node(root[0] if root[0] else 0) if root else None
    cur, next = [head], []
    while cur and index < len(root):
        for node in cur:
            if node is None:
                continue
            children: List[Node | None] = [None, None]
            for i in range(2):
                val = root[index + i]
                if val is not None:
                    children[i] = Node(val)
            index += 2
            node.left = children[0]
            node.right = children[1]
            next.extend(children)
        cur, next = next, []
    res: List[int | str] = []
    node, nextNode = Solution().connect(head), None
    while node:
        ans: List[int | str] = []
        while node:
            ans.append(node.val)
            if nextNode is None:
                nextNode = node.left
            node = node.next
        res.extend(ans)
        res.append("#")
        node, nextNode = nextNode, None
    print(res)


# []
polyfill(root=[])

# [1,#,2,3,#,4,5,7,#]
polyfill(root=[1, 2, 3, 4, 5, None, 7])
