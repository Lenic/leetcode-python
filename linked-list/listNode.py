from typing import List, Optional
from typing_extensions import Self

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x: int = 0, next: Self | None = None):
        self.val = x
        self.next = next


class BidirectionalListNode(ListNode):
    def __init__(self, x: int = 0, next: Self | None = None, prev: Self | None = None):
        super().__init__(x, next)
        self.prev = prev


def convertArray(data: List[int]) -> Optional[ListNode]:
    cur = dummy = ListNode()
    for val in data:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next


def convertLinkedList(head: Optional[ListNode]) -> List[int]:
    ans: List[int] = []
    while head:
        ans.append(head.val)
        head = head.next
    return ans
