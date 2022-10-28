from typing import List, Optional


from utils import convertTree, TreeNode


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        mapper = {val: index for index, val in enumerate(inorder)}

        def build(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            node = TreeNode(postorder.pop())
            index = mapper.get(node.val)
            if index is None:
                return None
            node.right = build(index + 1, right)
            node.left = build(left, index - 1)
            return node

        return build(0, len(inorder) - 1)


def polyfill(inorder: List[int], postorder: List[int]):
    print(convertTree(Solution().buildTree(inorder, postorder)))


# [3,9,20,None,None,15,7]
polyfill(inorder=[9, 3, 15, 20, 7], postorder=[9, 15, 7, 20, 3])
