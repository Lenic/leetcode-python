from typing import List, Optional
from typing_extensions import Self

from queue import Queue

from listNode import convertArray, ListNode


class TreeNode:
    def __init__(self, val: int = 0, left: Self | None = None, right: Self | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head is None:
            return None

        count, cur = 0, head
        while cur is not None:
            count += 1
            cur = cur.next

        cur = head

        def buildTree(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            mid = left + ((right - left) >> 1)
            node = TreeNode(mid)
            node.left = buildTree(left, mid - 1)
            nonlocal cur
            node.val = cur.val
            if cur.next:
                cur = cur.next
            node.right = buildTree(mid + 1, right)
            return node

        return buildTree(0, count - 1)


def polyfill(head: List[int]):
    res = Solution().sortedListToBST(convertArray(head))
    if res is None:
        print("[]")
    else:
        ans: List[int | None] = []
        q: Queue[TreeNode | None] = Queue()
        q.put(res)
        while not q.empty():
            item = q.get()
            ans.append(item.val if item is not None else None)
            if item and (item.left or item.right):
                q.put(item.left)
                q.put(item.right)
        print(ans)


# [0,-3,9,-10,null,5]
polyfill(head=[-10, -3, 0, 5, 9])

# [5]
# polyfill(head=[5])
