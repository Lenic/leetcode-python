from typing import List, Tuple


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        # 初始化 DP Table 二维矩阵：
        # - status[i][j] 是数学表示法 [i, j] 包含的范围
        # - 默认全部值都是 True
        status: List[List[int]] = [[True] * n for _ in range(n)]

        # 初始将第一个字符作为结果
        resLen = 1
        res: Tuple[int, int] = (0, 0)
        # 从子串长度为 2 的开始预处理回文子串，i 表示子串的长度
        for subLen in range(2, n + 1):
            # j 表示
            for i in range(n):
                # 找到以 i 为起始索引，长度为 subLen 子串的右侧索引值
                j = i + subLen - 1
                # 索引值越界就停止
                if j >= n:
                    break
                # 基于上个状态的结果计算当前状态的结果
                status[i][j] = s[i] == s[j] and status[i + 1][j - 1]
                # 只有当前计算结果是回文子串，并且长度比结果子串更长时，才做替换操作
                if status[i][j] and subLen > resLen:
                    # 更新最新的结果子串长度
                    resLen = subLen
                    # 存储当前子串的左右索引值
                    res = (i, j)

        return s[res[0] : res[1] + 1]


# "bb"
print(Solution().longestPalindrome("bb"))

# "aca"
print(Solution().longestPalindrome("aacabdkacaa"))

# "b"
print(Solution().longestPalindrome("bc"))

# "b"
print(Solution().longestPalindrome("b"))

# "bab"
print(Solution().longestPalindrome("babad"))

# "bb"
print(Solution().longestPalindrome("cbbd"))
