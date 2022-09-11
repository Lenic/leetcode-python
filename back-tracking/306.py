from typing import List


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def getValue(left: int, right: int) -> int:
            sum = 0
            for i in range(left, right):
                sum = sum * 10 + ord(num[i]) - ord("0")
            return sum

        def dfs(ans: List[int], previous: int, index: int):
            if index == n:
                return previous == -1

            sum = previous
            prefixSum = ans[-1] + ans[-2]

            for i in range(index, n):
                if sum == -1:
                    sum = getValue(i, i + 1)
                elif sum == 0:
                    return False
                else:
                    sum = sum * 10 + getValue(i, i + 1)

                if prefixSum == sum:
                    ans.append(sum)
                    return dfs(ans, -1, i + 1)
                elif prefixSum < sum:
                    return False
                else:
                    return dfs(ans, sum, i + 1)

        for i in range(1, n - 1):
            if (i > 1) and (num[0] == "0"):
                break

            for j in range(i + 1, n):
                if (i + 1 != j) and (num[i] == "0"):
                    break

                if dfs([getValue(0, i), getValue(i, j)], -1, j):
                    return True
        return False


# False
print(Solution().isAdditiveNumber("0235813"))

# False
print(Solution().isAdditiveNumber("1203"))

# True
print(Solution().isAdditiveNumber("000"))

# False
print(Solution().isAdditiveNumber("1023"))

# True
print(Solution().isAdditiveNumber("199100199"))

# True
print(Solution().isAdditiveNumber("112358"))
