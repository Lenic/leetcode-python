from typing import Any, List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        n, m = len(matrix), len(matrix[0])
        self.prefixSums = [[0] * (m + 1)]
        for i in range(n):
            s = [0]
            for val in matrix[i]:
                s.append(s[-1] + val)
            self.prefixSums.append([(self.prefixSums[i][j] + s[j]) for j in range(m + 1)])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        aa = self.prefixSums[row2 + 1][col2 + 1]
        at = self.prefixSums[row1][col2 + 1]
        al = self.prefixSums[row2 + 1][col1]
        ai = self.prefixSums[row1][col1]

        return aa - at - al + ai


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


def polyfill(names: List[str], data: List[Any]):
    obj: NumMatrix | None = None
    res: List[Any] = []

    for i in range(len(names)):
        if names[i] == "NumMatrix":
            obj = NumMatrix(*data[i])
            res.append(None)
        elif names[i] == "sumRegion" and obj is not None:
            res.append(obj.sumRegion(*data[i]))

    print(res)


# [null, 8, 11, 12]
polyfill(
    ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"],
    [
        [[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]],
        [2, 1, 4, 3],
        [1, 1, 2, 2],
        [1, 2, 2, 4],
    ],
)
