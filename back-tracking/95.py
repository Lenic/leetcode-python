from typing import List, Optional
from typing_extensions import Self


class TreeNode:
    def __init__(self, val: int = 0, left: Optional[Self] = None, right: Optional[Self] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def traversal(start: int, end: int) -> List[Optional[TreeNode]]:
            if start > end:
                return [None]

            ans: List[Optional[TreeNode]] = []
            for i in range(start, end + 1):
                leftTrees = traversal(start, i - 1)
                rightTrees = traversal(i + 1, end)

                for l in leftTrees:
                    for r in rightTrees:
                        node = TreeNode(i)
                        node.left = l
                        node.right = r
                        ans.append(node)

            return ans

        return traversal(1, n)


print(Solution().generateTrees(3))
