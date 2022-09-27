from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 字符串的长度
        n = len(s)
        # 获取字典中字符串的最短和最长
        dictCounts = [len(val) for val in wordDict]
        minCount = min(dictCounts)
        maxCount = max(dictCounts)
        # 将字典转成不可重复的集合
        cache: set[str] = set(wordDict)
        # 状态数组：第一个表示空字符串时是匹配的
        data = [True] + [False] * n
        for i in range(n):
            for j in range(i + minCount, min(i + maxCount + 1, n + 1)):
                if data[i] and s[i:j] in cache:
                    data[j] = True

        return data[-1]


# True
print(Solution().wordBreak("bb", ["a", "b", "bbb", "bbbb"]))

# True
print(Solution().wordBreak("aaaaaaa", ["aaaa", "aaa"]))

# False
print(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))

# True
print(Solution().wordBreak("leetcode", ["leet", "code"]))

# True
print(Solution().wordBreak("applepenapple", ["apple", "pen"]))
