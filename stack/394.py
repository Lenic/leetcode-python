from typing import List


class Solution:
    def decodeString(self, s: str) -> str:
        ans: List[str] = []
        previous: List[int] = [0]

        for i in range(len(s)):
            item = s[i]
            if ord("0") <= ord(item) <= ord("9"):
                if i > 0 and ord("0") <= ord(s[i - 1]) <= ord("9"):
                    previous[-1] = previous[-1] * 10 + ord(item) - ord("0")
                else:
                    previous.append(ord(item) - ord("0"))
            elif item == "[":
                ans.append("[")
            elif item == "]":
                fragment = []
                while True:
                    inner = ans.pop()
                    if inner == "[":
                        break
                    else:
                        fragment.append(inner)

                content = "".join(fragment[::-1])
                for i in range(previous.pop()):
                    ans.append(content)
            else:
                ans.append(item)

        return "".join(ans)


# accaccaccefef
print(Solution().decodeString("3[a2[c]]2[ef]"))

# abccdcdcdxyz
print(Solution().decodeString("abc3[cd]xyz"))

# abcabccdcdcdef
print(Solution().decodeString("2[abc]3[cd]ef"))

# aaabcbc
print(Solution().decodeString("3[a]2[bc]"))
