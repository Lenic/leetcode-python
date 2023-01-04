from typing import List, Optional
from typing_extensions import Self

from listNode import convertArray, convertLinkedList, ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        left = right = dummy = ListNode(0, head)
        for _ in range(n):
            if right:
                right = right.next
            else:
                return head
        while right and right.next:
            right = right.next
            if left:
                left = left.next
        if left and left.next:
            left.next = left.next.next
        return dummy.next


def polyfill(data: List[int], n: int):
    cur = convertArray(data)
    res = Solution().removeNthFromEnd(cur, n)
    print(convertLinkedList(res))


# []
polyfill([1], 1)

# [1,2,3,5]
polyfill([1, 2, 3, 4, 5], 2)

# [1]
polyfill([1, 2], 1)
