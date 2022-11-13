from typing import List, Optional

from utils import convertArray, TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans: List[List[int]] = []
        if root is None:
            return ans
        cur, next = [root], []
        while cur:
            res: List[int] = []
            for item in cur:
                if item is None:
                    continue
                res.append(item.val)
                next.append(item.left)
                next.append(item.right)
            if res:
                ans.append(res)
            cur, next = next, []
        return ans


def polyfill(root: List[int | None]):
    print(Solution().levelOrder(convertArray(root)))


# [[3],[9,20],[15,7]]
polyfill(root=[3, 9, 20, None, None, 15, 7])
