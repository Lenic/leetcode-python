from typing import List, Optional
from listNode import convertArray, ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry, dummy = 0, ListNode()
        res = dummy
        while l1 or l2 or carry:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry = 1 if val > 9 else 0
            if carry:
                val = val % 10
            res.next = ListNode(val)
            res = res.next
        return dummy.next


def polyfill(l1: List[int], l2: List[int]):
    res = Solution().addTwoNumbers(convertArray(l1), convertArray(l2))
    if not res:
        print("[]")
    else:
        ans: List[int] = []
        while res:
            ans.append(res.val)
            res = res.next
        print(ans)


# [7,0,8]
polyfill(l1=[2, 4, 3], l2=[5, 6, 4])

# [0]
polyfill(l1=[0], l2=[0])

# [8,9,9,9,0,0,0,1]
polyfill(l1=[9, 9, 9, 9, 9, 9, 9], l2=[9, 9, 9, 9])
