from typing import List, Optional
from listNode import convertArray, convertLinkedList, ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        if dummy.next is None:
            return None
        cur = dummy.next
        while cur.next:
            next = cur.next
            cur.next = next.next
            dummy.next, next.next = next, dummy.next
        return dummy.next


def polyfill(head: List[int]):
    res = Solution().reverseList(convertArray(head))
    print(convertLinkedList(res))


# [1]
polyfill([1])

# [5,4,3,2,1]
polyfill([1, 2, 3, 4, 5])
