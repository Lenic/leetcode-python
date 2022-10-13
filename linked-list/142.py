from typing import List, Optional
from typing_extensions import Self

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x: int, next: Self | None = None):
        self.val = x
        self.next = next


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        slow = fast = head
        while True:
            slowNext = slow.next
            if slowNext != None:
                slow = slowNext
            for _ in range(2):
                fastNext = fast.next
                if fastNext != None:
                    fast = fastNext
                else:
                    return None
            if slow is fast:
                break
        p = head
        while p != slow:
            pNext = p.next
            if pNext != None:
                p = pNext
            slowNext = slow.next
            if slowNext != None:
                slow = slowNext
        return p


def polyfill(data: List[int], pos: int):
    cur = node = ListNode(0)
    for val in data:
        cur.next = ListNode(val)
        cur = cur.next

    if pos != -1:
        cycle = node
        for _ in range(pos + 1):
            next = cycle.next
            if next != None:
                cycle = next
            else:
                break
        cur.next = cycle

    res = Solution().detectCycle(node.next)
    print(res.val if res != None else "null")


# 2
polyfill([3, 2, 0, -4], 1)

# null
polyfill([1], -1)

# 1
polyfill([1, 2], 0)
