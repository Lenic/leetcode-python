from typing import List, Any

import random


class Solution:
    original: List[int]
    current: List[int]

    def __init__(self, nums: List[int]):
        self.original = nums
        self.current = nums.copy()

    def reset(self) -> List[int]:
        self.current = self.original.copy()
        return self.current

    def shuffle(self) -> List[int]:
        ans = self.current.copy()
        for i in range(len(self.current) - 1, 0, -1):
            index = random.randrange(i + 1)
            ans[index], ans[i] = ans[i], ans[index]
        self.current = ans
        return ans


def polyfill(names: List[str], nums: List[Any]):
    obj = Solution(nums[0][0])
    ans: List[None | List[int]] = [None]
    for i in range(1, len(names)):
        key = names[i]
        if key == "reset":
            ans.append(obj.reset())
        elif key == "shuffle":
            ans.append(obj.shuffle())
    print(ans)


# [null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]
polyfill(["Solution", "shuffle", "reset", "shuffle"], [[[1, 2, 3]], [], [], []])
