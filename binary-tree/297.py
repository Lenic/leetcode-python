from typing import List, Optional

from collections import deque


from utils import convertArray, convertTree, TreeNode


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        ans: List[int | None] = []
        if root is None:
            return "[]"
        q: deque[TreeNode | None] = deque([root])
        while q:
            n, hasChildren = len(q), False
            for _ in range(n):
                node = q.popleft()
                if node is None:
                    ans.append(None)
                    continue
                ans.append(node.val)
                q.append(node.left)
                q.append(node.right)
                if not hasChildren:
                    hasChildren = node.left is not None or node.right is not None
            if not hasChildren:
                break
        while ans[-1] is None:
            ans.pop()
        return f"[{','.join(str(val) for val in ans)}]"

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) <= 2:
            return None

        converted: deque[int | None] = deque([])
        for val in data[1:-1].split(","):
            if val == "None":
                converted.append(None)
            else:
                converted.append(int(val))

        root = TreeNode(converted.popleft() or 0)
        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                children: List[TreeNode | None] = [None, None]
                for i in range(2):
                    if not converted:
                        break
                    val = converted.popleft()
                    if val is not None:
                        newNode = TreeNode(val)
                        children[i] = newNode
                        q.append(newNode)
                node.left = children[0]
                node.right = children[1]
        return root


def polyfill(root: List[int | None]):
    ser = Codec()
    deser = Codec()
    print(convertTree(deser.deserialize(ser.serialize(convertArray(root)))))


# [1,2]
polyfill(root=[1, 2])

# [1,2,3,None,None,4,5]
polyfill(root=[1, 2, 3, None, None, 4, 5])

# []
polyfill(root=[])

# [1]
polyfill(root=[1])
