from typing import Generator, List

from collections import deque


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited: List[bool] = [False] * len(rooms)
        visited[0] = True
        stack: deque[int] = deque([0])

        def getNeighbors(i: int) -> Generator[int, None, None]:
            for neighbor in rooms[i]:
                if not visited[neighbor]:
                    yield neighbor

        while stack:
            try:
                room = next(getNeighbors(stack[-1]))
                visited[room] = True
                stack.append(room)
            except StopIteration:
                stack.pop()

        return all(visited)


# True
print(Solution().canVisitAllRooms([[1], [2], [3], []]))

# False
print(Solution().canVisitAllRooms(rooms=[[1, 3], [3, 0, 1], [2], [0]]))
