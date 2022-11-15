from typing import Any, List

from collections import deque


class MyStack:
    cur: deque[int]
    bak: deque[int]

    def __init__(self):
        self.cur = deque([])
        self.bak = deque([])

    def push(self, x: int) -> None:
        self.cur.append(x)

    def pop(self) -> int:
        for _ in range(len(self.cur) - 1):
            self.bak.append(self.cur.popleft())
        val = self.cur.pop()
        self.bak, self.cur = self.cur, self.bak
        return val

    def top(self) -> int:
        for _ in range(len(self.cur) - 1):
            self.bak.append(self.cur.popleft())
        item = self.cur.popleft()
        self.bak.append(item)
        self.bak, self.cur = self.cur, self.bak
        return item

    def empty(self) -> bool:
        return len(self.cur) == 0


def polyfill(names: List[str], values: List[Any]):
    obj, ans = MyStack(), []

    for i, name in enumerate(names):
        match name:
            case "MyStack":
                ans.append(None)
            case "push":
                obj.push(*values[i])
                ans.append(None)
            case "pop":
                ans.append(obj.pop())
            case "top":
                ans.append(obj.top())
            case "empty":
                ans.append(obj.empty())
    print(ans)


# [null, null, null, 2, 2, false]
polyfill(["MyStack", "push", "push", "top", "pop", "empty"], [[], [1], [2], [], [], []])
