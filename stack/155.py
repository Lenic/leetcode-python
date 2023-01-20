from typing import Any, List

from sys import maxsize


class MinStack:
    data: List[int]
    mins: List[int]

    def __init__(self):
        self.data = []
        self.mins = [maxsize]

    def push(self, val: int) -> None:
        self.data.append(val)
        self.mins.append(min(self.mins[-1], val))

    def pop(self) -> None:
        self.data.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.mins[-1]


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


# [null,null,-1,-1]
polyfill(["MinStack", "push", "top", "getMin"], [[], [-1], [], []])

# [null,null,null,null,-2,-1,null,-2]
polyfill(["MinStack", "push", "push", "push", "getMin", "top", "pop", "getMin"], [[], [-2], [0], [-1], [], [], [], []])

# [null,null,null,null,-3,null,0,-2]
polyfill(["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"], [[], [-2], [0], [-3], [], [], [], []])
