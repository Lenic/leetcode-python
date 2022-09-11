from math import ceil
from typing import List, Any


class NumArray:
    def __init__(self, nums: List[int]):
        n = len(nums)
        segmentSize = int(n**0.5)
        self.segmentSize = segmentSize

        self.data = nums
        self.sums = [0] * ceil(n / segmentSize)

        remainder = -1
        segmentIndex = 0
        for index in range(n):
            remainder += 1
            if remainder == segmentSize:
                remainder = 0
                segmentIndex += 1

            self.sums[segmentIndex] += nums[index]

    def update(self, index: int, val: int) -> None:
        self.data[index] = val

        segmentIndex = index // self.segmentSize
        self.sums[segmentIndex] = sum(
            self.data[segmentIndex * self.segmentSize : (segmentIndex + 1) * self.segmentSize]
        )

    def sumRange(self, left: int, right: int) -> int:
        if left == right:
            return self.data[left]

        leftSegmentIndex = left // self.segmentSize
        rightSegmentIndex = right // self.segmentSize

        if leftSegmentIndex == rightSegmentIndex:
            return sum(self.data[left : right + 1])

        currentSum = sum(self.data[left : (leftSegmentIndex + 1) * self.segmentSize])
        currentSum += sum(self.sums[leftSegmentIndex + 1 : rightSegmentIndex])
        currentSum += sum(self.data[rightSegmentIndex * self.segmentSize : right + 1])

        return currentSum


def polyfill(actions: List[str], nums: List[List[Any]]):
    obj: NumArray | None = None

    res: List[Any] = []
    for index, action in enumerate(actions):
        if action == "NumArray":
            obj = NumArray(nums[index][0])
            res.append("null")
        elif action == "sumRange":
            if obj != None:
                res.append(obj.sumRange(nums[index][0], nums[index][1]))
        elif action == "update":
            if obj != None:
                obj.update(nums[index][0], nums[index][1])
                res.append("null")
    print(res)


# [null, 9, null, 8]
polyfill(["NumArray", "sumRange", "update", "sumRange"], [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]])

# [null,-121,null,118,-104,null,null,-221,-293,null,null]
polyfill(
    [
        "NumArray",
        "sumRange",
        "update",
        "sumRange",
        "sumRange",
        "update",
        "update",
        "sumRange",
        "sumRange",
        "update",
        "update",
    ],
    [
        [[-28, -39, 53, 65, 11, -56, -65, -39, -43, 97]],
        [5, 6],
        [9, 27],
        [2, 3],
        [6, 7],
        [1, -82],
        [3, -72],
        [3, 7],
        [1, 8],
        [5, 13],
        [4, -67],
    ],
)

# [null,3,15,7,null,null,null,12,null,5,null]
polyfill(
    [
        "NumArray",
        "sumRange",
        "sumRange",
        "sumRange",
        "update",
        "update",
        "update",
        "sumRange",
        "update",
        "sumRange",
        "update",
    ],
    [[[0, 9, 5, 7, 3]], [4, 4], [2, 4], [3, 3], [4, 5], [1, 7], [0, 8], [1, 2], [1, 9], [4, 4], [3, 4]],
)

# [null,-1,null,1]
polyfill(["NumArray", "sumRange", "update", "sumRange"], [[[-1]], [0, 0], [0, 1], [0, 0]])
