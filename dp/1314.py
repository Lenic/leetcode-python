from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        prefixSums = []
        for item in mat:
            prefixSum = [0]
            for val in item:
                prefixSum.append(prefixSum[-1] + val)
            prefixSums.append(prefixSum)

        r, c = len(mat), len(mat[0])
        ans: List[List[int]] = [[0] * c for _ in range(r)]
        for i in range(r):
            vt, vb = max(0, i - k), min(r, i + k + 1)
            for j in range(c):
                hl, hr = max(0, j - k), min(c, j + k + 1)
                ans[i][j] = sum((prefixSums[row][hr] - prefixSums[row][hl]) for row in range(vt, vb))
        return ans


# [[731, 731, 731], [930, 930, 930], [930, 930, 930], [930, 930, 930], [721, 721, 721]]
print(Solution().matrixBlockSum([[67, 64, 78], [99, 98, 38], [82, 46, 46], [6, 52, 55], [55, 99, 45]], 3))

# [[12, 21, 16], [27, 45, 33], [24, 39, 28]]
print(Solution().matrixBlockSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1))
