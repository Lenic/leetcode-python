from collections import deque


class Solution:
    dic = {")": "(", "]": "[", "}": "{"}

    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack: deque[str] = deque([])
        for val in s:
            if val == "(" or val == "[" or val == "{":
                stack.append(val)
            elif not len(stack) or stack.pop() != self.dic[val]:
                return False
        return len(stack) == 0


# false
print(Solution().isValid("([)]"))

# false
print(Solution().isValid("(]"))

# true
print(Solution().isValid("()[]{}"))

# true
print(Solution().isValid("()"))
