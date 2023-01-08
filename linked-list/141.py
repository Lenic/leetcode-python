from typing import List, Optional

from listNode import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = ListNode(next=head)
        while fast and fast.next:
            fast = fast.next.next
            if slow:
                slow = slow.next
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
