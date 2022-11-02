from typing import Callable, Generator, List

from collections import deque


class Solution:
    minNumber: int = ord("0")
    maxNumber: int = ord("9")

    def getSymbol(self, input: str, cb: Callable[[int], int]) -> str:
        val = cb(ord(input))
        if self.minNumber <= val <= self.maxNumber:
            return chr(val)
        elif val < self.minNumber:
            return "9"
        else:
            return "0"

    def getValues(self, val: str) -> Generator[str, None, None]:
        s = list(val)
        for i in range(4):
            original = s[i]
            s[i] = self.getSymbol(original, lambda x: x - 1)
            yield "".join(s)
            s[i] = self.getSymbol(original, lambda x: x + 1)
            yield "".join(s)
            s[i] = original

    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0
        dead = set(deadends)
        if "0000" in dead:
            return -1

        visited, dead = {"0000"}, set(deadends)
        q: deque[tuple[str, int]] = deque([("0000", 0)])
        while q:
            cur, step = q.popleft()
            for val in self.getValues(cur):
                if val == target:
                    return step + 1
                if val not in visited and val not in dead:
                    q.append((val, step + 1))
                    visited.add(val)
        return -1


# 6
print(Solution().openLock(deadends=["0201", "0101", "0102", "1212", "2002"], target="0202"))
