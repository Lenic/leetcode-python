from typing import List, Optional


from utils import convertArray, TreeNode


class Solution:
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
        if root is None:
            return None

        parents: dict[int, TreeNode] = {}

        def dfs(parent: TreeNode):
            if parent.left:
                parents[parent.left.val] = parent
                dfs(parent.left)
            if parent.right:
                parents[parent.right.val] = parent
                dfs(parent.right)

        dfs(root)

        visited: dict[int, bool] = {}
        next = p
        while next:
            visited[next.val] = True
            next = parents.get(next.val)
        next = q
        while next:
            if visited.get(next.val):
                return next
            next = parents.get(next.val)
        return None


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
