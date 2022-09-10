from typing import List, Optional
from typing_extensions import Self


class TreeNode:
    """力扣专属的二叉树节点"""

    def __init__(self, val: int = 0, left: Optional[Self] = None, right: Optional[Self] = None):
        # type: (int, Optional[TreeNode], Optional[TreeNode]) -> None
        self.val = val
        self.left = left
        self.right = right


def convertToTree(nums: List[Optional[int]]):
    """转换力扣专属的数字数组为二叉树"""

    def fill(index: int, count: int) -> List[Optional[TreeNode]]:
        if index >= len(nums):
            return []

        currentCount: int = 0
        ans: List[Optional[TreeNode]] = []
        for i in range(index, 1 if index == 0 else index + count * 2):
            if i >= len(nums):
                break

            item = nums[i]
            if item == None:
                ans.append(None)
            else:
                currentCount += 1
                ans.append(TreeNode(item))

        children = fill(index + len(ans), currentCount)
        if len(children) > 0:
            childIndex = -1

            def getChild():
                nonlocal childIndex
                childIndex += 1
                return children[childIndex] if childIndex < len(children) else None

            for item in ans:
                if item == None:
                    continue

                item.left = getChild()
                item.right = getChild()

        return ans

    return fill(0, 0)[0]
