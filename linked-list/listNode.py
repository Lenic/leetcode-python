from typing_extensions import Self

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x: int = 0, next: Self | None = None):
        self.val = x
        self.next = next
