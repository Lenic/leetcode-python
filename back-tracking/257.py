from typing import List, Optional
from helper import TreeNode, convertToTree


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res: List[str] = []

        def dfs(ans: List[int], node: Optional[TreeNode]):
            if node == None:
                return

            unchanged = True
            ans.append(node.val)

            if node.left != None:
                unchanged = False
                dfs(ans, node.left)

            if node.right != None:
                unchanged = False
                dfs(ans, node.right)

            if unchanged:
                res.append("->".join(str(val) for val in ans))

            ans.pop()

        dfs([], root)
        return res


def polyfill(data: List[Optional[int]]) -> None:
    root = convertToTree(data)
    print(Solution().binaryTreePaths(root))


# ['1->2->5', '1->3']
polyfill([1, 2, 3, None, 5])

# ['1']
polyfill([1])
