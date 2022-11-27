from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans: List[str] = []
        for i in range(min(len(val) for val in strs)):
            item = strs[0][i]
            if all(val[i] == item for val in strs):
                ans.append(item)
            else:
                break
        return "".join(ans)


# fl
print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))

# ''
print(Solution().longestCommonPrefix(["dog", "racecar", "car"]))
