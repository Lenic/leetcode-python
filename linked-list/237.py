from typing import List, Optional

from listNode import ListNode, convertArray, convertLinkedList


class Solution:
    def deleteNode(self, node: ListNode):
        next = node.next
        if next is None:
            return
        node.val = next.val
        node.next = next.next


def polyfill(head: List[int], node: int):
    dummy = ListNode(0, convertArray(head))
    cur = dummy.next
    while cur and cur.val != node:
        cur = cur.next
    if cur:
        Solution().deleteNode(cur)
    print(convertLinkedList(dummy.next))


# [4,1,9]
polyfill(head=[4, 5, 1, 9], node=5)

# [4,5,9]
polyfill(head=[4, 5, 1, 9], node=1)
