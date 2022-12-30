class Solution:
    def myAtoi(self, s: str) -> int:
        l, h, n = -(2**31), 2**31 - 1, len(s)
        ans, positive = 0, None
        i = 0
        while i < n:
            if s[i] == " ":
                i += 1
                continue
            if s[i].isdigit():
                ans, positive = ord(s[i]) - ord("0"), True
            elif s[i] == "+":
                positive = True
            elif s[i] == "-":
                positive = False
            else:
                return 0
            i += 1
            break
        while i < n:
            if s[i].isdigit():
                ans, i = ans * 10 - ord("0") + ord(s[i]), i + 1
                if ans >= h:
                    if positive:
                        return h
                    else:
                        if i + 1 < n and s[i + 1].isdigit():
                            return l
                        ans *= -1
                        if ans <= l:
                            return l
                        else:
                            return ans
            else:
                break
        return ans if positive else ans * -1


# 0
print(Solution().myAtoi(".1"))

# 4193
print(Solution().myAtoi("4193 with words"))

# -42
print(Solution().myAtoi("   -42"))

# 42
print(Solution().myAtoi("42"))
