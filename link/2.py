from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry, current = 0, ListNode()
        head = current

        while l1 or l2 or carry:
            sum = carry
            if l1:
                sum += l1.val
                l1 = l1.next

            if l2:
                sum += l2.val
                l2 = l2.next

            if sum > 9:
                sum -= 10
                carry = 1
            else:
                carry = 0

            current.next = ListNode(sum)
            current = current.next

        return head.next


def polyfill(l1: List[int], l2: List[int]):
    link1 = ListNode()
    c1 = link1
    for val in l1:
        c1.next = ListNode(val)
        c1 = c1.next

    link2 = ListNode()
    c2 = link2
    for val in l2:
        c2.next = ListNode(val)
        c2 = c2.next

    response = Solution().addTwoNumbers(link1.next, link2.next)

    res: List[int] = []
    while response:
        res.append(response.val)
        response = response.next
    return res


print(polyfill([2, 4, 3], [5, 6, 4]))
