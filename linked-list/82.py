from typing import List, Optional

from listNode import convertArray, convertLinkedList, ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        cur = dummy = ListNode(head.val - 1, head)
        while cur.next and cur.next.next:
            n1, n2 = cur.next, cur.next.next
            if n1.val != n2.val:
                cur = n1
            else:
                while n2.next:
                    n2 = n2.next
                    if n2.val != n1.val:
                        cur.next = n2
                        break
                if cur.next is not n2:
                    cur.next = None
        return dummy.next


def polyfill(head: List[int]):
    print(convertLinkedList(Solution().deleteDuplicates(convertArray(head))))


# []
polyfill([1, 1, 1])

# [1,2,5]
polyfill([1, 2, 3, 3, 4, 4, 5])

# [2,3]
polyfill([1, 1, 1, 2, 3])

# [1,2,5]
polyfill([1, 2, 3, 3, 4, 4, 5])

# []
polyfill([1, 1])

# [1]
polyfill([1])
