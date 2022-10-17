from typing import List, Optional
from typing_extensions import Self

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: Self | None = None, random: Self | None = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if head is None:
            return None

        cache: dict[Node, int] = dict()
        cur = head
        while cur:
            cache[cur] = len(cache)
            cur = cur.next

        cur = dummy = Node(0)
        cache2: dict[int, Node] = dict()
        origin = head
        while origin:
            cur.next = Node(origin.val)
            cur = cur.next
            origin = origin.next
            cache2[len(cache2)] = cur

        cur = dummy.next
        while head and cur:
            if head.random is not None:
                index = cache[head.random]
                if index is not None:
                    cur.random = cache2[index]
            cur = cur.next
            head = head.next

        return dummy.next


def polyfill(data: List[List[None | int]]):
    cur = dummy = Node(0)
    cache: List[Node] = []
    for i in range(len(data)):
        cur.next = Node(data[i][0] or 0)
        cur = cur.next
        cache.append(cur)
    for i in range(len(data)):
        randomIndex = data[i][1]
        if randomIndex is not None:
            cache[i].random = cache[randomIndex]
    res = Solution().copyRandomList(dummy.next)
    if res is None:
        print("[]")
    else:
        cache2: dict[Node, int] = dict()
        cur = res
        while cur:
            cache2[cur] = len(cache2)
            cur = cur.next
        ans: List[List[int | None]] = []
        while res:
            ans.append([res.val, cache2.get(res.random) if res.random is not None else None])
            res = res.next
        print(ans)
    pass


# [[7,null],[13,0],[11,4],[10,2],[1,0]]
polyfill([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
