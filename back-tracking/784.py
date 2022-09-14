from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res: List[str] = []

        def dfs(ans: List[str], index: int):
            if index == len(s):
                res.append("".join(ans))
                return

            ans.append(s[index])
            dfs(ans, index + 1)
            ans.pop()

            upper = s[index].upper()
            if upper != s[index]:
                ans.append(upper)
                dfs(ans, index + 1)
                ans.pop()

            lower = s[index].lower()
            if lower != s[index]:
                ans.append(lower)
                dfs(ans, index + 1)
                ans.pop()

        dfs([], 0)
        return res


# ["a1b2", "a1B2", "A1b2", "A1B2"]
print(Solution().letterCasePermutation("a1b2"))

# ["C", "c"]
print(Solution().letterCasePermutation("C"))
