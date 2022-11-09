from typing import List, Optional
from typing_extensions import Self


class Node:
    def __init__(self, val: int = 0, neighbors: List[Self] | None = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if node is None:
            return None

        hash: dict[int, List[int]] = {}
        visited: set[int] = set()

        def dfs(cur: Node):
            if cur.val in visited:
                return
            visited.add(cur.val)
            hash[cur.val] = list(map(lambda x: x.val, cur.neighbors))
            for neighbor in cur.neighbors:
                dfs(neighbor)

        dfs(node)

        hash2: dict[int, Node] = {}
        for i in range(1, len(hash) + 1):
            hash2[i] = Node(i)
        for i, val in hash.items():
            cur = hash2[i]
            for neighbor in list(map(lambda x: hash2[x], val)):
                cur.neighbors.append(neighbor)
        return hash2[1]


def polyfill(adjList: List[List[int]]):
    hash: dict[int, Node] = {}
    for i in range(1, len(adjList) + 1):
        hash[i] = Node(i)
    for i, val in enumerate(adjList):
        if len(val):
            cur = hash[i + 1]
            for neighbor in list(map(lambda x: hash[x], val)):
                if neighbor not in cur.neighbors:
                    cur.neighbors.append(neighbor)
    res = Solution().cloneGraph(hash[1] if len(hash) else None)
    if res is None:
        print("[]")
    else:
        ans: dict[int, List[int]] = {}
        visited: set[int] = set()

        def dfs(cur: Node):
            if cur.val in visited:
                return
            visited.add(cur.val)
            ans[cur.val] = list(map(lambda x: x.val, cur.neighbors))
            for neighbor in cur.neighbors:
                dfs(neighbor)

        dfs(res)
        print([ans[i] for i in range(1, len(ans) + 1)])


# [[2,4],[1,3],[2,4],[1,3]]
polyfill(adjList=[[2, 4], [1, 3], [2, 4], [1, 3]])

# [[]]
polyfill(adjList=[[]])

# []
polyfill(adjList=[])
