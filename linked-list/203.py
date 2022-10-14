from typing import List, Optional

from listNode import ListNode


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None

        previous = dummy = ListNode(next=head)
        cur = head

        while cur:
            if cur.val == val:
                previous.next = cur = cur.next
            else:
                previous, cur = cur, cur.next

        return dummy.next


def polyfill(data: List[int], val: int):
    cur = dummy = ListNode()
    for item in data:
        cur.next = ListNode(item)
        cur = cur.next
    res = Solution().removeElements(dummy.next, val)
    if not res:
        print("[]")
    else:
        ans: List[int] = []
        while res:
            ans.append(res.val)
            res = res.next
        print(ans)


# []
polyfill([], 1)

# [1]
polyfill([1], 1)

# [2]
polyfill([1, 2], 1)

# [1]
polyfill([1, 2], 2)

# [1, 2, 3, 4, 5]
polyfill([1, 2, 6, 3, 4, 5, 6], 6)
