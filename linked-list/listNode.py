from typing import List, Optional
from typing_extensions import Self

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x: int = 0, next: Self | None = None):
        self.val = x
        self.next = next


class BidirectionalListNode(ListNode):
    def __init__(self, x: int = 0, next: Self | None = None, prev: Self | None = None):
        super().__init__(x, next)
        self.prev = prev


def convertArray(data: List[int]) -> Optional[ListNode]:
    cur = dummy = ListNode()
    for val in data:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next


def convertLinkedList(head: Optional[ListNode]) -> List[int]:
    ans: List[int] = []
    while head:
        ans.append(head.val)
        head = head.next
    return ans


class TreeNode:
    def __init__(self, val: int = 0, left: Self | None = None, right: Self | None = None):
        self.val = val
        self.left = left
        self.right = right


def convertArrayToTree(data: List[int | None]) -> Optional[TreeNode]:
    """根据数组按照层序遍历的方式生成一棵树"""
    if not data:
        return None

    item = data[0]
    if item is None:
        raise Exception("the index of 0 can't be none.")

    index, root = 1, TreeNode(item)
    nodes = [root]
    while nodes and index < len(data):
        ans: List[TreeNode | None] = []
        for cur in nodes:
            if cur is None:
                continue
            if index == len(data):
                break
            item = data[index]
            if item is not None:
                cur.left = TreeNode(item)
                ans.append(cur.left)
            if index + 1 == len(data):
                break
            item = data[index + 1]
            if item is not None:
                cur.right = TreeNode(item)
                ans.append(cur.right)
            index += 2
        nodes = ans
    return root
