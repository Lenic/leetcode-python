class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev, i, n, base = -1, 0, len(s), ord("0")
        while i < n:
            if not s[i].isdigit():
                i += 1
            else:
                cur = 0
                while i < n and s[i].isdigit():
                    cur, i = cur * 10 + ord(s[i]) - base, i + 1
                if cur > prev:
                    prev = cur
                else:
                    return False
        return True


# true
print(Solution().areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles"))

# false
print(Solution().areNumbersAscending("hello world 5 x 5"))
