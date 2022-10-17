from typing import List, Optional

from listNode import convertArray, convertLinkedList, ListNode


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or head is None:
            return head
        count, cur = 1, head
        while cur and cur.next:
            cur = cur.next
            count += 1
        cur.next = head
        k = k % count
        for _ in range(count - k - 1):
            if head and head.next:
                head = head.next
        node = head.next
        head.next = None
        return node


def polyfill(data: List[int], k: int):
    print(convertLinkedList(Solution().rotateRight(convertArray(data), k)))


# [4,5,1,2,3]
polyfill([1, 2, 3, 4, 5], 2)

# [5,1,2,3,4]
polyfill([1, 2, 3, 4, 5], 1)

# [2,0,1]
polyfill([0, 1, 2], 4)
