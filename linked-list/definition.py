from typing import List
from typing_extensions import Self


class LinkedNode:
    def __init__(self, val: int = 0, next: Self | None = None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = self.tail = LinkedNode()

    def get(self, index: int) -> int:
        if index < self.size:
            cur = self.head
            for _ in range(index + 1):
                node = cur.next
                if node != None:
                    cur = node
                else:
                    break
            return cur.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        self.size += 1
        self.head.next = LinkedNode(val, self.head.next)
        if self.head is self.tail:
            self.tail = self.head.next

    def addAtTail(self, val: int) -> None:
        self.size += 1
        node = LinkedNode(val)
        self.tail.next = node
        self.tail = node

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        elif 0 < index < self.size:
            self.size += 1
            cur = self.head
            for _ in range(index):
                node = cur.next
                if node != None:
                    cur = node
                else:
                    break
            cur.next = LinkedNode(val, cur.next)

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self.size:
            cur = self.head
            for _ in range(index):
                node = cur.next
                if node != None:
                    cur = node
                else:
                    break
            target = cur.next
            if target != None:
                cur.next = target.next
            if cur.next == None:
                self.tail = cur
            self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


def polyfill(names: List[str], values: List[List[int]]):
    res: List[int | str] = []
    obj = MyLinkedList()
    for i in range(len(names)):
        match names[i]:
            case "MyLinkedList":
                res.append("null")
            case "get":
                res.append(obj.get(*values[i]))
            case "addAtHead":
                obj.addAtHead(*values[i])
                res.append("null")
            case "addAtTail":
                obj.addAtTail(*values[i])
                res.append("null")
            case "addAtIndex":
                obj.addAtIndex(*values[i])
                res.append("null")
            case "deleteAtIndex":
                obj.deleteAtIndex(*values[i])
                res.append("null")
    print(res)


# ['null', 'null', -1]
polyfill(["MyLinkedList", "addAtIndex", "get"], [[], [1, 0], [0]])

# ['null', 'null', 'null', -1]
polyfill(
    ["MyLinkedList", "addAtHead", "deleteAtIndex", "get"],
    [[], [3], [0], [1]],
)

# ['null', 'null', 'null', 'null', 2, 'null', 3]
polyfill(
    ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"],
    [[], [1], [3], [1, 2], [1], [1], [1]],
)

# ['null', 'null', 'null', 2, 'null', 'null', 2, 'null', -1, 'null', 5, 'null']
polyfill(
    [
        "MyLinkedList",
        "addAtHead",
        "addAtIndex",
        "get",
        "addAtHead",
        "addAtTail",
        "get",
        "addAtTail",
        "get",
        "addAtHead",
        "get",
        "addAtHead",
    ],
    [[], [5], [1, 2], [1], [6], [2], [3], [1], [5], [2], [2], [6]],
)
