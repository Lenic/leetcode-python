from typing import List, Optional
from typing_extensions import Self

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x: int, next: Self | None = None):
        self.val = x
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow = head
        fast = slow.next
        while fast:
            slowNode = slow.next
            if slowNode:
                slow = slowNode
            for _ in range(2):
                fastNode = fast.next
                if fastNode:
                    fast = fastNode
                else:
                    return False
            if slow is fast:
                return True
        return False


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

    print(Solution().hasCycle(node.next))


# True
polyfill([3, 2, 0, -4], 1)

# False
polyfill([1], -1)
