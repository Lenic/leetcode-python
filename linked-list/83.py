from typing import List, Optional

from listNode import convertArray, convertLinkedList, ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head


def polyfill(head: List[int]):
    print(convertLinkedList(Solution().deleteDuplicates(convertArray(head))))


# [1,2]
polyfill([1, 1, 2])

# [1,2,3]
polyfill([1, 1, 2, 3, 3])
