from typing import Optional, List
from typing_extensions import Self


class Node:
    def __init__(self, val: int = 0, left: Self | None = None, right: Self | None = None, next: Self | None = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        cur, next = [root], []
        while cur:
            prev, hasValue = Node(), False
            for node in cur:
                if node is None:
                    continue
                hasValue = True
                prev.next, prev = node, node
                next.extend([node.left, node.right])
            cur, next = next if hasValue else [], []
        return root


def polyfill(root: List[int]):
    index, head = 1, Node(root[0])
    cur, next = [head], []
    while cur and index < len(root):
        for node in cur:
            children: List[Node | None] = [None, None]
            for i in range(2):
                children[i] = Node(root[index + i])
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


# [1,#,2,3,#,4,5,6,7,#]
polyfill(root=[1, 2, 3, 4, 5, 6, 7])
