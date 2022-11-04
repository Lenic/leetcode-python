from typing import Any


class MinStack:
    data: list[int]
    minStack: list[int]

    def __init__(self):
        self.data = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.data.append(val)
        if not self.minStack:
            self.minStack.append(val)
        elif val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        if not self.data:
            return
        val = self.data.pop()
        if val == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        if self.data:
            return self.data[-1]
        return -1

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        return -1


def polyfill(names: list[str], values: list[Any]):
    ans, obj = [], MinStack()
    for index, name in enumerate(names):
        match name:
            case "MinStack":
                ans.append("null")
            case "push":
                obj.push(*values[index])
                ans.append("null")
            case "pop":
                obj.pop()
                ans.append("null")
            case "top":
                ans.append(obj.top())
            case "getMin":
                ans.append(obj.getMin())
    print(ans)


# [null,null,null,null,-2,-1,null,-2]
polyfill(["MinStack", "push", "push", "push", "getMin", "top", "pop", "getMin"], [[], [-2], [0], [-1], [], [], [], []])

# [null,null,null,null,-3,null,0,-2]
polyfill(["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"], [[], [-2], [0], [-3], [], [], [], []])
