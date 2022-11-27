class Solution:
    def longestPalindrome(self, s: str) -> str:
        begin = end = 0

        def findIndexes(left: int, right: int) -> tuple[int, int]:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return (left + 1, right - 1)

        for i in range(len(s) - 1):
            for l, r in [findIndexes(i, i), findIndexes(i, i + 1)]:
                if r - l > end - begin:
                    begin, end = l, r
        return s[begin : end + 1]


# "bab"
print(Solution().longestPalindrome("babad"))

# "bb"
print(Solution().longestPalindrome("cbbd"))
