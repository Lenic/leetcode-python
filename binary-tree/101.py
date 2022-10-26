from typing import Callable, List, Optional

from utils import convertArray, TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def dfs(
            ans: List[int | None], node: Optional[TreeNode], getChild: Callable[[TreeNode, bool], Optional[TreeNode]]
        ):
            if node is None:
                ans.append(None)
                return
            ans.append(node.val)
            dfs(ans, getChild(node, True), getChild)
            dfs(ans, getChild(node, False), getChild)

        leftAnswers, rightAnswers = [], []
        dfs(leftAnswers, root.left, lambda node, isLeft: node.left if isLeft else node.right)
        dfs(rightAnswers, root.right, lambda node, isLeft: node.right if isLeft else node.left)

        if len(leftAnswers) != len(rightAnswers):
            return False
        for i in range(len(leftAnswers)):
            if leftAnswers[i] != rightAnswers[i]:
                return False
        return True


def polyfill(root: List[int | None]):
    print(Solution().isSymmetric(convertArray(root)))


# True
polyfill(root=[4, -57, -57, None, 67, 67, None, None, -97, -97])

# True
polyfill(root=[1, 2, 2, 3, 4, 4, 3])

# False
polyfill(root=[1, 2, 2, None, 3, None, 3])
