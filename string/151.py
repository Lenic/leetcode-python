class Solution:
    def reverseWords(self, s: str) -> str:
        left, stack = 0, []
        for i in range(1, len(s)):
            prev, cur = s[i - 1], s[i]
            if prev == " " and cur != " ":
                left = i
            elif prev != " " and cur == " ":
                stack.append(s[left:i])
                left = i
        if s[-1] != " ":
            stack.append(s[left:])
        return " ".join(stack[::-1])


# "blue is sky the"
print(Solution().reverseWords(s="the sky is blue"))

# "world hello"
print(Solution().reverseWords(s="  hello world  "))

# "example good a"
print(Solution().reverseWords(s="a good   example"))
