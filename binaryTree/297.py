from typing import List, Optional

from collections import deque

from utils import convertArray, convertTree, TreeNode


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        ans: List[str] = []
        if not root:
            return ""
        q: deque[TreeNode | None] = deque([root])
        while len(q):
            node = q.popleft()
            if node is None:
                ans.append("null")
            else:
                ans.append(str(node.val))
                q.extend([node.left, node.right])
        return ",".join(ans)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        nodes = list(map(lambda x: None if x == "null" else TreeNode(int(x)), data.split(",")))
        i, q = 1, deque([nodes[0]])
        while len(q):
            for _ in range(len(q)):
                cur = q.popleft()
                if cur is not None:
                    children: List[TreeNode | None] = [None] * 2
                    for j in range(i, min(len(nodes), i + 2)):
                        children[j - i] = nodes[j]
                        q.append(nodes[j])
                    cur.left = children[0]
                    cur.right = children[1]
                    i += 2
        return nodes[0]


def polyfill(root: List[int | None]):
    ser = Codec()
    deser = Codec()
    print(convertTree(deser.deserialize(ser.serialize(convertArray(root)))))


# [4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]
polyfill(
    root=[
        4,
        -7,
        -3,
        None,
        None,
        -9,
        -3,
        9,
        -7,
        -4,
        None,
        6,
        None,
        -6,
        -6,
        None,
        None,
        0,
        6,
        5,
        None,
        9,
        None,
        None,
        -1,
        -4,
        None,
        None,
        None,
        -2,
    ]
)

# [1,2]
polyfill(root=[1, 2])

# [1,2,3,None,None,4,5]
polyfill(root=[1, 2, 3, None, None, 4, 5])

# []
polyfill(root=[])

# [1]
polyfill(root=[1])
