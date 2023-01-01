from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans, i, m, n = [], 0, len(strs), min(len(val) for val in strs)
        while i < n:
            j, val = 1, strs[0][i]
            while j < m:
                if val != strs[j][i]:
                    return "".join(ans)
                j += 1
            if j == m:
                ans.append(val)
            i += 1
        return "".join(ans)


# fl
print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))

# ""
print(Solution().longestCommonPrefix(["dog", "racecar", "car"]))
