from typing import List


class Solution:
    def decodeString(self, s: str) -> str:
        baseCodeN = ord("0")
        baseCodeA = ord("a")

        index = 0
        ans: List[str] = []
        countList: List[int] = []
        while index < len(s):
            if 0 <= ord(s[index]) - baseCodeN <= 9:
                count = 0
                while 0 <= ord(s[index]) - baseCodeN <= 9:
                    count = count * 10 + ord(s[index]) - baseCodeN
                    index += 1
                countList.append(count)
            elif 0 <= ord(s[index]) - baseCodeA <= 26:
                mid = ""
                while index < len(s) and 0 <= ord(s[index]) - baseCodeA <= 26:
                    mid += s[index]
                    index += 1
                ans.append(mid)
            elif s[index] == "[":
                ans.append("[")
                index += 1
            elif s[index] == "]":
                fragmentList: List[str] = []
                while ans[-1] != "[":
                    fragmentList.append(ans.pop())
                ans.pop()
                fragment = "".join(fragmentList[::-1])
                ans.append("".join(fragment for _ in range(countList.pop())))
                index += 1
        return "".join(ans)


# "abccdcdcdxyz"
print(Solution().decodeString("abc3[cd]xyz"))

# "abcabccdcdcdef"
print(Solution().decodeString("2[abc]3[cd]ef"))

# "accaccacc"
print(Solution().decodeString("3[a2[c]]"))

# "aaabcbc"
print(Solution().decodeString("3[a]2[bc]"))
