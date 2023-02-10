from typing import List
from collections import Counter, defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans, pattern, cur, left = [], Counter(p), defaultdict(int), 0

        def isEqual() -> bool:
            for key in pattern:
                if cur[key] != pattern[key]:
                    return False
            return True

        for right, val in enumerate(s):
            cur[val] += 1
            if right - left + 1 > len(p):
                cur[s[left]] -= 1
                left += 1
            if right - left + 1 == len(p) and isEqual():
                ans.append(left)
        return ans


# [0, 1, 2]
print(Solution().findAnagrams(s="abab", p="ab"))

# [0, 6]
print(Solution().findAnagrams(s="cbaebabacd", p="abc"))
