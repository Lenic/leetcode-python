from typing import List

from collections import defaultdict


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans: List[str] = []
        if len(s) <= 10:
            return ans
        cache: defaultdict[str, int] = defaultdict(int)
        for i in range(10, len(s) + 1):
            cache[s[i - 10 : i]] += 1
        for key, val in cache.items():
            if val > 1:
                ans.append(key)
        return ans


# ["AAAAAAAAAA"]
print(Solution().findRepeatedDnaSequences("AAAAAAAAAAA"))

# ["AAAAACCCCC","CCCCCAAAAA"]
print(Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))

# ["AAAAAAAAAA"]
print(Solution().findRepeatedDnaSequences("AAAAAAAAAAAAA"))
