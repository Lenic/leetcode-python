class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        ans, prev = [], self.countAndSay(n - 1)
        i, c = 0, len(prev)
        while i < c:
            val = prev[i]
            j = i + 1
            while j < c and prev[j] == val:
                j += 1
            ans.append(f"{j - i}{val}")
            i = j
        return "".join(ans)


# "1"
print(Solution().countAndSay(1))

# "1211"
print(Solution().countAndSay(4))
