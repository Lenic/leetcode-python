from typing import List, Optional

from listNode import convertArray, convertLinkedList, ListNode


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        slow = fast = dummy = ListNode(0, head)
        while fast and fast.next:
            for _ in range(k):
                if fast and fast.next:
                    fast = fast.next
                else:
                    return dummy.next
            anchor = slow.next
            while slow and slow.next is not fast:
                target = slow.next
                if target is not None:
                    slow.next = target.next
                    if fast is not None:
                        target.next = fast.next
                        fast.next = target
            slow = fast = anchor
        return dummy.next


def polyfill(head: List[int], k: int):
    print(convertLinkedList(Solution().reverseKGroup(convertArray(head), k)))


# [3,2,1,4,5]
polyfill(head=[1, 2, 3, 4, 5], k=3)
