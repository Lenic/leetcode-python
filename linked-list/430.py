from typing import List, Optional
from typing_extensions import Self


class Node:
    def __init__(self, val: int = 0, prev: Self | None = None, next: Self | None = None, child: Self | None = None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None
        dummy = Node(0, None, None, None)

        def traversal(node: Node, res: Node):
            while True:
                target = Node(node.val, res, None, None)
                res.next = target
                res = target
                if node.child:
                    res = traversal(node.child, target)
                if node.next:
                    node = node.next
                else:
                    break
            return res

        traversal(head, dummy)
        if dummy.next:
            dummy.next.prev = None
        return dummy.next


def polyfill(head: List[int | None]):
    node = row = dummy = Node()
    for i in range(len(head)):
        cur = head[i]
        prev = None if i == 0 else head[i - 1]

        if cur is not None and prev is None and i != 0:
            row.child = Node(cur)
            node = row = row.child
        elif cur is not None:
            target = Node(cur, None if node is dummy else node)
            node.next = target
            node = node.next
            if i == 0:
                row = target
        elif cur is None and prev is None:
            if row.next:
                row = row.next

    res = Solution().flatten(dummy.next)
    if not res:
        print("[]")
    else:
        ans: List[int] = []
        while res:
            ans.append(res.val)
            res = res.next
        print(ans)


# [1,2,3,7,8,11,12,9,10,4,5,6]
polyfill([1, 2, 3, 4, 5, 6, None, None, None, 7, 8, 9, 10, None, None, 11, 12])
