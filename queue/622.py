from typing import Any


class MyCircularQueue:
    head: int
    tail: int
    data: list[int]

    def __init__(self, k: int):
        self.data = [0] * k
        self.head = self.tail = -1

    def enQueue(self, value: int) -> bool:
        nextTail = (self.tail + 1) % len(self.data)
        if nextTail != self.head:
            self.data[nextTail], self.tail = value, nextTail
            if self.head == -1:
                self.head = 0
            return True
        return False

    def deQueue(self) -> bool:
        if self.head < 0:
            return False

        if self.head == self.tail:
            self.head = self.tail = -1
        else:
            self.head = (self.head + 1) % len(self.data)
        return True

    def Front(self) -> int:
        return self.data[self.head] if self.head >= 0 else -1

    def Rear(self) -> int:
        return self.data[self.tail] if self.tail >= 0 else -1

    def isEmpty(self) -> bool:
        return self.head == self.tail == -1

    def isFull(self) -> bool:
        return (self.tail + 1) % len(self.data) == self.head


def polyfill(names: list[str], value: list[Any]):
    ans, obj = [], MyCircularQueue(1)
    for i, name in enumerate(names):
        match name:
            case "MyCircularQueue":
                obj = MyCircularQueue(*value[i])
                ans.append("null")
            case "enQueue":
                ans.append(obj.enQueue(*value[i]))
            case "deQueue":
                ans.append(obj.deQueue(*value[i]))
            case "Front":
                ans.append(obj.Front())
            case "Rear":
                ans.append(obj.Rear())
            case "isEmpty":
                ans.append(obj.isEmpty())
            case "isFull":
                ans.append(obj.isFull())
    print(ans)


# [null,true,true,true,false,3,true,true,true,4]
polyfill(
    ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"],
    [[3], [1], [2], [3], [4], [], [], [], [4], []],
)
