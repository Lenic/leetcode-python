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
        cur = root
        while cur:
            node = dummy = Node()
            while cur:
                if cur.left:
                    node.next, node = cur.left, cur.left
                if cur.right:
                    node.next, node = cur.right, cur.right
                cur = cur.next
            cur = dummy.next
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
                if index + i >= len(root):
                    break
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
                nextNode = node.left or node.right
            node = node.next
        res.extend(ans)
        res.append("#")
        node, nextNode = nextNode, None
    print(res)


# [7,#,-10,2,#,-4,3,-8,#,-1,11,#]
polyfill(root=[7, -10, 2, -4, 3, -8, None, None, None, None, -1, 11])

# [1,#,2,3,#,4,5,6,#,7,8,#]
polyfill(root=[1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8])

# [1,#,2,3,#,4,5,7,#]
polyfill(root=[1, 2, 3, 4, 5, None, 7])

# []
polyfill(root=[])
