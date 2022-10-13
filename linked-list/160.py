from typing import List, Optional
from typing_extensions import Self

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x: int = 0, next: Self | None = None):
        self.val = x
        self.next = next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        countA = countB = 1
        curA = headA
        while curA.next:
            countA += 1
            curA = curA.next
        curB = headB
        while curB.next:
            countB += 1
            curB = curB.next
        if not (curA is curB):
            return None
        if countA > countB:
            for _ in range(countA - countB):
                node = headA.next
                if node:
                    headA = node
        elif countA < countB:
            for _ in range(countB - countA):
                node = headB.next
                if node:
                    headB = node
        while not (headA is headB):
            nodeA = headA.next
            if nodeA:
                headA = nodeA
            nodeB = headB.next
            if nodeB:
                headB = nodeB
        return headA


def polyfill(intersectVal: int, listA: List[int], listB: List[int], skipA: int, skipB: int):
    headA, headB = ListNode(), ListNode()
    cur = intersectNode = headA
    for i in range(len(listA)):
        val = listA[i]
        cur.next = ListNode(val)
        cur = cur.next
        if i == skipA and val == intersectVal:
            intersectNode = cur
    cur = headB
    for i in range(len(listB)):
        val = listB[i]
        if i == skipB and val == intersectVal:
            cur.next = intersectNode
            break
        cur.next = ListNode(val)
        cur = cur.next
    if headA.next and headB.next:
        res = Solution().getIntersectionNode(headA.next, headB.next)
        print(res.val if res != None else "null")


# 1
polyfill(1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 0, 0)

# 8
polyfill(intersectVal=8, listA=[4, 1, 8, 4, 5], listB=[5, 6, 1, 8, 4, 5], skipA=2, skipB=3)

# 2
polyfill(intersectVal=2, listA=[1, 9, 1, 2, 4], listB=[3, 2, 4], skipA=3, skipB=1)
