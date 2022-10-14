from typing import List, Optional

from listNode import ListNode


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        if head.next is None:
            return True
        cache: List[int] = []
        slow = fast = ListNode(next=head)
        while fast:
            nodeFast = fast.next
            nodeFast = nodeFast.next if nodeFast else None
            if nodeFast:
                fast = nodeFast
            else:
                break
            node = slow.next
            if node:
                slow = node
                cache.append(node.val)
        if fast and fast.next:
            fast = fast.next
            slow = slow.next
        index = len(cache) - 1
        while slow:
            slow = slow.next
            if not slow:
                break
            if slow.val == cache[index]:
                index -= 1
        return index == -1


def polyfill(data: List[int]):
    cur = dummy = ListNode()
    for item in data:
        cur.next = ListNode(item)
        cur = cur.next
    print(Solution().isPalindrome(dummy.next))


# True
polyfill([1, 2, 2, 1])

# False
polyfill([1, 2])
