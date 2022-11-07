from typing import List


class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            int(s)
            return True
        except:
            pass
        return False

    def evalRPN(self, tokens: List[str]) -> int:
        stack: List[int] = []
        for val in tokens:
            if self.isNumber(val):
                stack.append(int(val))
            else:
                r, l = stack.pop(), stack.pop()
                if val == "+":
                    stack.append(l + r)
                elif val == "-":
                    stack.append(l - r)
                elif val == "*":
                    stack.append(l * r)
                elif val == "/":
                    stack.append(int(l / r))
        return stack[-1]


# 22
print(Solution().evalRPN(tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))

# 6
print(Solution().evalRPN(tokens=["4", "13", "5", "/", "+"]))

# 9
print(Solution().evalRPN(tokens=["2", "1", "+", "3", "*"]))
