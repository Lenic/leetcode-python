from typing import List, Optional


from utils import convertArray, TreeNode


class Solution:
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
        if root is None:
            return None

        def dfs(ans: List[TreeNode], parent: Optional[TreeNode], targetValue: int) -> bool:
            if parent is None:
                return False

            ans.append(parent)
            if targetValue == parent.val:
                return True

            res: bool = False
            if parent.left is not None:
                res = dfs(ans, parent.left, targetValue)
            if res is not True and parent.right is not None:
                res = dfs(ans, parent.right, targetValue)

            if res is not True:
                ans.pop()
            return res

        pPath: List[TreeNode] = []
        dfs(pPath, root, p.val)

        qPath: List[TreeNode] = []
        dfs(qPath, root, q.val)

        minCount = min(len(pPath), len(qPath))
        for i in range(minCount):
            if pPath[i].val != qPath[i].val:
                return pPath[i - 1]
        return pPath[minCount - 1]


def polyfill(root: List[int | None], p: int, q: int):
    res = Solution().lowestCommonAncestor(convertArray(root), TreeNode(p), TreeNode(q))
    print(res.val if res else "None")


# 1
polyfill(root=[1, 2], p=2, q=1)

# 1
polyfill(root=[1, 2], p=1, q=2)

# 5
polyfill(root=[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], p=5, q=4)

# 3
polyfill(root=[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], p=5, q=1)
