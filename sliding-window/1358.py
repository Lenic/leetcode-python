class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans, n, baseIndex = 0, len(s), ord("a")
        pre = [[0] * (n + 1) for _ in range(3)]
        for i in range(n):
            for j in range(3):
                pre[j][i + 1] = pre[j][i]
                pre[ord(s[i]) - baseIndex][i + 1] += 1
        for i in range(n):
            l, r, pos = i + 1, n, -1
            while l <= r:
                mid = l + ((r - l) >> 1)
                if pre[0][mid] - pre[0][i] > 0 and pre[1][mid] - pre[1][i] > 0 and pre[2][mid] - pre[2][i] > 0:
                    r = mid - 1
                    pos = mid
                else:
                    l = mid + 1
            if ~pos:
                ans += n - pos + 1
        return ans


# 11
print(Solution().numberOfSubstrings("acbbcac"))

# 1
print(Solution().numberOfSubstrings("abc"))

# 3
print(Solution().numberOfSubstrings("aaacb"))

# 10
print(Solution().numberOfSubstrings("abcabc"))
