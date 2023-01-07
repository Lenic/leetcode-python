from typing import List, Optional
from collections import deque

from listNode import convertArray, ListNode


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True
        stack: deque[int] = deque([])
        slow = fast = ListNode(0, head)
        while fast and fast.next:
            fast = fast.next.next
            if slow and slow.next:
                slow = slow.next
                stack.append(slow.val)
        if fast is None and len(stack):
            stack.pop()
        while slow and slow.next:
            slow = slow.next
            if slow.val != stack.pop():
                return False
        return True if len(stack) == 0 else False


def polyfill(data: List[int]):
    print(Solution().isPalindrome(convertArray(data)))


# True
polyfill([1, 0, 1])

# True
polyfill([1])

# False
polyfill([1, 0, 0])

# True
polyfill([1, 2, 2, 1])

# False
polyfill([1, 2])
