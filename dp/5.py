from typing import List, Tuple


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        def expandAroundCenter(left, right) -> Tuple[int, int]:
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        left, right = 0, 0
        for i in range(n):
            # 这里用于处理奇数长度的子串
            left1, right1 = expandAroundCenter(i, i)
            if right1 - left1 > right - left:
                left = left1
                right = right1
            # 这里用于处理偶数长度的子串
            left2, right2 = expandAroundCenter(i, i + 1)
            if right2 - left2 > right - left:
                left = left2
                right = right2

        return s[left : right + 1]


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
