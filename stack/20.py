class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []
        for val in list(s):
            if val == "(" or val == "[" or val == "{":
                stack.append(val)
            elif val == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif val == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            elif val == "}":
                if stack and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
        return False if len(stack) else True


# False
print(Solution().isValid(s="}"))

# True
print(Solution().isValid(s="()[]{}"))

# False
print(Solution().isValid(s="["))

# False
print(Solution().isValid(s="[[]"))

# False
print(Solution().isValid(s="(]"))

# True
print(Solution().isValid(s="()"))
