from typing import List, Optional

from listNode import ListNode


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        self.cur = head

        def traversal(node: ListNode) -> bool:
            if node.next and not traversal(node.next):
                return False
            if node.val == self.cur.val:
                if self.cur.next:
                    self.cur = self.cur.next
                return True
            else:
                return False

        return traversal(head)


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
