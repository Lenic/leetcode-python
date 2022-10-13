from typing import List, Optional
from typing_extensions import Self

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x: int = 0, next: Self | None = None):
        self.val = x
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        slow = fast = dummy = ListNode(0, head)
        for _ in range(n):
            if fast:
                fast = fast.next
            else:
                break

        while fast and fast.next:
            fast = fast.next
            node = slow.next
            if node:
                slow = node

        if slow.next:
            node = slow.next
            if node:
                slow.next = node.next

        return dummy.next


def polyfill(data: List[int], n: int):
    cur = head = ListNode()
    for val in data:
        cur.next = ListNode(val)
        cur = cur.next
    res = Solution().removeNthFromEnd(head.next, n)
    ans: List[int] = []
    while res:
        ans.append(res.val)
        res = res.next
    print(ans)


# []
polyfill([1], 1)

# [1,2,3,5]
polyfill([1, 2, 3, 4, 5], 2)
