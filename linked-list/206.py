from typing import List, Optional
from listNode import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode(next=head)
        cur = head.next
        while cur:
            head.next = cur.next
            tmp = dummy.next
            dummy.next = cur
            cur.next = tmp
            cur = head.next
        return dummy.next


def polyfill(head: List[int]):
    cur = dummy = ListNode()
    for val in head:
        cur.next = ListNode(val)
        cur = cur.next
    res = Solution().reverseList(dummy.next)
    if not res:
        print("[]")
    else:
        ans: List[int] = []
        while res:
            ans.append(res.val)
            res = res.next
        print(ans)


# [1]
polyfill([1])

# [5,4,3,2,1]
polyfill([1, 2, 3, 4, 5])
