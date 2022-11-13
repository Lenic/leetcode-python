from typing import List, Optional

from utils import convertArray, TreeNode


class Solution:
    def reverse(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        previous: Optional[TreeNode] = None
        while node:
            next, node.right = node.right, previous
            previous, node = node, next
        return previous

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans: List[int] = []
        head = TreeNode(left=root)
        while head:
            if head.left is None:
                head = head.right
            else:
                mostRight = head.left
                while mostRight.right is not None and mostRight.right is not head:
                    mostRight = mostRight.right
                if mostRight.right is None:
                    mostRight.right = head
                    head = head.left
                if mostRight.right is head:
                    mostRight.right = None
                    cur = node = self.reverse(head.left)
                    while cur:
                        ans.append(cur.val)
                        cur = cur.right
                    self.reverse(node)
                    head = head.right
        return ans


def polyfill(root: List[int | None]):
    print(Solution().postorderTraversal(convertArray(root)))


# [3,2,1]
polyfill(root=[1, None, 2, 3])

# []
polyfill(root=[])
