from typing import List, Optional


from utils import convertTree, TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mapper = {val: index for index, val in enumerate(inorder)}

        def build(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            node = TreeNode(preorder.pop(0))
            index = mapper[node.val]
            node.left = build(left, index - 1)
            node.right = build(index + 1, right)
            return node

        return build(0, len(preorder) - 1)


def polyfill(preorder: List[int], inorder: List[int]):
    print(convertTree(Solution().buildTree(preorder, inorder)))


# [3,9,20,None,None,15,7]
polyfill(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7])
