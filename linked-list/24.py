from typing import List, Optional
from typing_extensions import Self

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Self | None = None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy
        while cur:
            slow = cur.next
            if not slow:
                break
            fast = slow.next
            if not fast:
                break

            slow.next = fast.next
            fast.next = slow
            cur.next = fast
            cur = slow
        return dummy.next


def polyfill(data: List[int]):
    cur = head = ListNode()
    for val in data:
        cur.next = ListNode(val)
        cur = cur.next

    node = Solution().swapPairs(head.next)

    res: List[int] = []
    while node:
        res.append(node.val)
        node = node.next
    print(res)


# [2,1,4,3]
polyfill([1, 2, 3, 4])

# []
polyfill([])

# [1]
polyfill([1])
