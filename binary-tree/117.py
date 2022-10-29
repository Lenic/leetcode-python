from typing import Optional, List
from typing_extensions import Self


class Node:
    def __init__(self, val: int = 0, left: Self | None = None, right: Self | None = None, next: Self | None = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        cur, prev, next = root, None, None
        while cur:
            # 处理前一个元素的 next 指针
            if prev is not None:
                link = cur.left or cur.right
                if link:
                    prevLink = prev.right or prev.left
                    if prevLink:
                        prevLink.next = link
                    prev = cur
            # 更新前一个元素的引用
            else:
                prev = cur
            # 关联当前节点的左子树的 next 到右子树
            if cur.left:
                cur.left.next = cur.right
            # 更新下一行的行首元素指针
            if next is None:
                next = cur.left or cur.right
            # 切换到当前行下一个元素继续
            if cur.next:
                cur = cur.next
            # 当前行最后一个元素时的处理逻辑
            else:
                prev, cur, next = None, next, None
        return root


def polyfill(root: List[int | None]):
    index, head = 1, Node(root[0] if root[0] else 0) if root else None
    cur, next = [head], []
    while cur and index < len(root):
        for node in cur:
            if node is None:
                continue
            children: List[Node | None] = [None, None]
            for i in range(2):
                if index + i >= len(root):
                    break
                val = root[index + i]
                if val is not None:
                    children[i] = Node(val)
            index += 2
            node.left = children[0]
            node.right = children[1]
            next.extend(children)
        cur, next = next, []
    res: List[int | str] = []
    node, nextNode = Solution().connect(head), None
    while node:
        ans: List[int | str] = []
        while node:
            ans.append(node.val)
            if nextNode is None:
                nextNode = node.left or node.right
            node = node.next
        res.extend(ans)
        res.append("#")
        node, nextNode = nextNode, None
    print(res)


# [7,#,-10,2,#,-4,3,-8,#,-1,11,#]
polyfill(root=[7, -10, 2, -4, 3, -8, None, None, None, None, -1, 11])

# [1,#,2,3,#,4,5,6,#,7,8,#]
polyfill(root=[1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8])

# [1,#,2,3,#,4,5,7,#]
polyfill(root=[1, 2, 3, 4, 5, None, 7])

# []
polyfill(root=[])
