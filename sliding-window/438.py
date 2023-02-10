from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans: List[int] = []
        if len(s) < len(p):
            return ans

        initialValue, pattern, cur = ord("a"), [0] * 26, [0] * 26
        for i in range(len(p)):
            pattern[ord(p[i]) - initialValue] += 1
            cur[ord(s[i]) - initialValue] += 1

        if pattern == cur:
            ans.append(0)

        for i in range(len(s) - len(p)):
            cur[ord(s[i]) - initialValue] -= 1
            cur[ord(s[i + len(p)]) - initialValue] += 1

            if pattern == cur:
                ans.append(i + 1)

        return ans


# []
print(Solution().findAnagrams(s="aa", p="bb"))

# [0, 1, 2]
print(Solution().findAnagrams(s="abab", p="ab"))

# [0, 6]
print(Solution().findAnagrams(s="cbaebabacd", p="abc"))
