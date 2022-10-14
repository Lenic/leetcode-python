from typing import List, Optional

from listNode import ListNode


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        no, oddDummy, evenDummy, dummy = 0, ListNode(), ListNode(), ListNode(next=head)
        cur, odd, even = dummy, oddDummy, evenDummy
        while cur:
            no += 1
            cur = cur.next
            if not cur:
                break
            if no % 2 == 1:
                odd.next = cur
                odd = odd.next
            else:
                even.next = cur
                even = even.next
        even.next = None
        odd.next = evenDummy.next
        return oddDummy.next


def polyfill(data: List[int]):
    cur = dummy = ListNode()
    for item in data:
        cur.next = ListNode(item)
        cur = cur.next
    res = Solution().oddEvenList(dummy.next)
    if not res:
        print("[]")
    else:
        ans: List[int] = []
        while res:
            ans.append(res.val)
            res = res.next
        print(ans)


# [1,3,5,2,4]
polyfill([1, 2, 3, 4, 5])

# [2,3,6,7,1,5,4]
polyfill([2, 1, 3, 5, 6, 4, 7])
