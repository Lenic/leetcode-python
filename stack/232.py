from typing import Any, List

from collections import deque


class MyQueue:
    cur: deque[int]
    bak: deque[int]

    def __init__(self):
        self.cur = deque([])
        self.bak = deque([])

    def push(self, x: int) -> None:
        self.cur.append(x)

    def pop(self) -> int:
        for _ in range(len(self.cur) - 1):
            self.bak.append(self.cur.pop())
        val = self.cur.pop()
        for _ in range(len(self.bak)):
            self.cur.append(self.bak.pop())
        return val

    def peek(self) -> int:
        return self.cur[0]

    def empty(self) -> bool:
        return len(self.cur) == 0


def polyfill(names: List[str], values: List[Any]):
    obj, ans = MyQueue(), []

    for i, name in enumerate(names):
        match name:
            case "MyQueue":
                ans.append(None)
            case "push":
                obj.push(*values[i])
                ans.append(None)
            case "pop":
                ans.append(obj.pop())
            case "peek":
                ans.append(obj.peek())
            case "empty":
                ans.append(obj.empty())
    print(ans)


# [null, null, null, 1, 1, false]
polyfill(["MyQueue", "push", "push", "peek", "pop", "empty"], [[], [1], [2], [], [], []])
