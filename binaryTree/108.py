from typing import List, Optional

from utils import convertTree, TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def buildTree(left: int, right: int):
            if left > right:
                return None
            mid = left + (right + 1 - left) // 2
            return TreeNode(nums[mid], buildTree(left, mid - 1), buildTree(mid + 1, right))

        mid = len(nums) // 2
        return TreeNode(nums[mid], buildTree(0, mid - 1), buildTree(mid + 1, len(nums) - 1))


# [0,-3,9,-10,null,5]
print(convertTree(Solution().sortedArrayToBST([-10, -3, 0, 5, 9])))

# [3,1]
print(convertTree(Solution().sortedArrayToBST([1, 3])))
