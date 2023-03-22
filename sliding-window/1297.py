from collections import defaultdict


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        cnt: defaultdict[str, int] = defaultdict(int)

        for right in range(minSize, len(s) + 1):
            letters: defaultdict[str, int] = defaultdict(int)

            left = right - minSize
            for i in range(left, right):
                letters[s[i]] += 1

            if len(letters) <= maxLetters:
                cnt[s[left:right]] += 1
            else:
                continue

            for i in range(left - 1, max(-1, left - (maxSize - minSize) - 1), -1):
                letters[s[i]] += 1

                if len(letters) <= maxLetters:
                    cnt[s[i:right]] += 1
                else:
                    break

        return 0 if len(cnt) == 0 else max(val for val in cnt.values())


# 0
print(Solution().maxFreq(s="abcde", maxLetters=2, minSize=3, maxSize=3))

# 3
print(Solution().maxFreq(s="aabcabcab", maxLetters=2, minSize=2, maxSize=3))

# 2
print(Solution().maxFreq(s="aaaa", maxLetters=1, minSize=3, maxSize=3))

# 2
print(Solution().maxFreq(s="aababcaab", maxLetters=2, minSize=3, maxSize=4))
