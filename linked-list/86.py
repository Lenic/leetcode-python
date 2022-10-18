from typing import List, Optional

from listNode import convertArray, convertLinkedList, ListNode


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        anchor = cur = dummy = ListNode(0, head)
        while cur:
            prev = cur
            cur = cur.next
            if cur is None:
                break
            elif cur.val < x:
                prev.next = cur.next
                cur.next = anchor.next
                anchor.next = cur
                anchor = cur
        return dummy.next


def polyfill(head: List[int], x: int):
    print(convertLinkedList(Solution().partition(convertArray(head), x)))


# [0,3,3,4,2,4,3]
polyfill([3, 3, 4, 2, 4, 0, 3], 1)

# [1,3]
polyfill(head=[3, 1], x=2)

# [1,2,2,4,3,5]
polyfill(head=[1, 4, 3, 2, 5, 2], x=3)

# [1,2]
polyfill(head=[2, 1], x=2)
