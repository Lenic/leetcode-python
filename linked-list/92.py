from typing import List, Optional

from listNode import convertArray, convertLinkedList, ListNode


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None
        anchor = ln = rn = dummy = ListNode(0, head)
        for i in range(right):
            if ln and i < left:
                anchor = ln
                ln = ln.next
            if rn:
                rn = rn.next
        rn = rn.next if rn else None
        while ln and ln.next is not rn:
            target = ln.next
            if not target:
                break
            ln.next = target.next
            target.next = anchor.next
            anchor.next = target

        return dummy.next


def polyfill(head: List[int], left: int, right: int):
    print(convertLinkedList(Solution().reverseBetween(convertArray(head), left, right)))


# [1,4,3,2,5]
polyfill(head=[1, 2, 3, 4, 5], left=2, right=4)

# [5]
polyfill(head=[5], left=1, right=1)
