from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans: List[str] = []

        def traversal(prefix: str, left: int, right: int):
            if left < right:
                return
            if left == n:
                cur = prefix
                for _ in range(n - right):
                    cur += ")"
                ans.append(cur)
                return
            traversal(prefix + "(", left + 1, right)
            traversal(prefix + ")", left, right + 1)

        traversal("(", 1, 0)
        return ans


# ["((()))","(()())","(())()","()(())","()()()"]
print(Solution().generateParenthesis(3))
