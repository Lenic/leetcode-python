from typing import Generator, List

from collections import deque


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        targetColor = image[sr][sc]
        if targetColor == color:
            return image

        def getNeighbors(i: int, j: int) -> Generator[tuple[int, int], None, None]:
            if i - 1 >= 0 and image[i - 1][j] == targetColor:
                yield (i - 1, j)
            if i + 1 < len(image) and image[i + 1][j] == targetColor:
                yield (i + 1, j)
            if j - 1 >= 0 and image[i][j - 1] == targetColor:
                yield (i, j - 1)
            if j + 1 < len(image[0]) and image[i][j + 1] == targetColor:
                yield (i, j + 1)

        stack: deque[tuple[int, int]] = deque([(sr, sc)])
        while stack:
            i, j = stack[-1]
            image[i][j] = color
            try:
                stack.append(next(getNeighbors(i, j)))
            except StopIteration:
                stack.pop()
        return image


# [[2,2,2],[2,2,0],[2,0,1]]
print(Solution().floodFill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, color=2))
