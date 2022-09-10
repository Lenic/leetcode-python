from typing import List, Optional
from typing_extensions import Self


class TreeNode:
    def __init__(self, val: int = 0, left: Optional[Self] = None, right: Optional[Self] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res: List[List[int]] = []

        def traversal(ans: List[int], node: Optional[TreeNode], sum: int):
            if node == None:
                return

            ans.append(node.val)
            currentSum = sum + node.val

            unchanged = True
            if node.left != None:
                unchanged = False
                traversal(ans, node.left, currentSum)
            if node.right != None:
                unchanged = False
                traversal(ans, node.right, currentSum)

            if unchanged and currentSum == targetSum:
                res.append(ans[:])

            ans.pop()

        traversal([], root, 0)
        return res


def polyfill(nums: List[Optional[int]], targetSum: int):
    def fill(index: int, count: int) -> List[Optional[TreeNode]]:
        if index >= len(nums):
            return []

        currentCount: int = 0
        ans: List[Optional[TreeNode]] = []
        for i in range(index, 1 if index == 0 else index + count * 2):
            if i >= len(nums):
                break

            if nums[i] == None:
                ans.append(None)
            else:
                currentCount += 1
                ans.append(TreeNode(nums[i]))

        children = fill(index + len(ans), currentCount)
        if len(children) > 0:
            childIndex = -1
            for item in ans:
                if item == None:
                    continue

                childIndex += 1
                item.left = children[childIndex] if childIndex < len(children) else None
                childIndex += 1
                item.right = children[childIndex] if childIndex < len(children) else None

        return ans

    root = fill(0, 0)[0]
    print(Solution().pathSum(root, targetSum))


# [[5,4,11,2],[5,8,4,5]]
polyfill([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22)

# []
polyfill([1, 2], 0)
