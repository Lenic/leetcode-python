from typing import List

from listNode import BidirectionalListNode


class MyLinkedList:
    def __init__(self):
        self.size, self.head, self.tail = 0, BidirectionalListNode(), BidirectionalListNode()

    def get(self, index: int) -> int:
        cur = self.head
        for _ in range(index + 1):
            node = cur.next
            if node != None:
                cur = node
            else:
                return -1
        return cur.val

    def addAtHead(self, val: int) -> None:
        self.addNode(self.head, val)

    def addAtTail(self, val: int) -> None:
        if self.tail.prev is None:
            self.addNode(self.head, val)
        else:
            self.addNode(self.tail.prev, val)

    def addNode(self, cur: BidirectionalListNode, val: int) -> None:
        node = BidirectionalListNode(val, cur.next, cur if cur is not self.head else None)
        if cur.next is None:
            self.tail.prev = node
        else:
            cur.next.prev = node
        cur.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.head
        for _ in range(index):
            if cur.next:
                cur = cur.next
            else:
                return
        self.addNode(cur, val)

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head
        for _ in range(index + 1):
            node = cur.next
            if node is not None:
                cur = node
            else:
                return
        if cur.prev is not None:
            cur.prev.next = cur.next
        if cur.next is not None:
            cur.next.prev = cur.prev
        if cur.next is None:
            self.tail.prev = cur.prev
        if cur.prev is None:
            self.head.next = cur.next


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
polyfill(
    ["MyLinkedList", "deleteAtIndex", "get"],
    [[], [0], [0]],
)

# ['null', 'null', 'null', -1]
polyfill(
    ["MyLinkedList", "addAtHead", "deleteAtIndex", "get"],
    [[], [2], [0], [0]],
)

# ['null', 'null', 'null', 2, 1]
polyfill(
    ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "deleteAtIndex", "get", "get"],
    [[], [2], [1], [1, 3], [1], [0], [1]],
)

# ['null', 'null', 2, 3, 1]
polyfill(
    ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "get", "get"],
    [[], [2], [1], [1, 3], [0], [1], [2]],
)

# ['null', 'null', 2, 3, 1]
polyfill(
    ["MyLinkedList", "addAtTail", "addAtHead", "addAtIndex", "get", "get", "get"],
    [[], [1], [2], [1, 3], [0], [1], [2]],
)

# ['null', 'null', 2, 3, 1]
polyfill(
    ["MyLinkedList", "addAtIndex", "addAtIndex", "addAtIndex", "get", "get", "get"],
    [[], [0, 1], [0, 2], [1, 3], [0], [1], [2]],
)

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
