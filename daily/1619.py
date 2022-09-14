from sys import maxsize
from typing import List
import heapq


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        heapLen = len(arr) * 5 // 100
        if heapLen < 1:
            return sum(arr) / len(arr)

        # 反向最大堆：存放最小的 5%
        maxList: List[int] = []
        # 反向最小堆：存放最大的 5%
        minList: List[int] = []
        # 剩余的元素集合
        restList: List[int] = []
        # 开始处理剩余的元素
        for val in arr:
            # 最小的 5% 中最大的元素：因为一开始列表没有元素，使用缺省值（所有数的最大值）替代
            maxInMin = -maxList[0] if len(maxList) > 0 else maxsize
            # 如果『最小的 5% 中最大的元素』还没有填满，首先应该填满：填满的过程中不做其它操作
            if len(maxList) < heapLen:
                heapq.heappush(maxList, -val)
                continue
            # 首先判断当前元素是否小于『最小的 5% 中最大的元素』
            if val < maxInMin:
                # 交换这两个元素
                val, maxList[0] = maxList[0], val
                # 因为『存放最小的 5% 元素的列表』内保存的都是『反值』，所以元值进去后需要取反
                maxList[0] *= -1
                # 同样的道理，取出的元素也需要取反后才能用
                val *= -1
                # 处理替换后的数据
                heapq.heapreplace(maxList, maxList[0])
            # 最大的 5% 中最小的元素：因为一开始列表没有元素，使用缺省值（所有数的最小值）替代
            minInMax = minList[0] if len(minList) > 0 else -maxsize
            # 如果『最大的 5% 中最小的元素』还没有填满，首先应该填满：填满的过程中不做其它操作
            if len(minList) < heapLen:
                heapq.heappush(minList, val)
                continue
            # 再判断当前元素是否大于『最大的 5% 中最小的元素』
            if val > minInMax:
                # 交换这两个元素：因为这里保存的是原值，所以不再需要取反
                val, minList[0] = minList[0], val
                # 处理替换后的数据
                heapq.heapreplace(minList, minList[0])
            # 经过上面两步处理后的元素，肯定是剩余的元素了，加入到剩余元素列表中
            restList.append(val)

        return sum(restList) / len(restList)


# 4.77778
print(
    Solution().trimMean(
        [
            6,
            0,
            7,
            0,
            7,
            5,
            7,
            8,
            3,
            4,
            0,
            7,
            8,
            1,
            6,
            8,
            1,
            1,
            2,
            4,
            8,
            1,
            9,
            5,
            4,
            3,
            8,
            5,
            10,
            8,
            6,
            6,
            1,
            0,
            6,
            10,
            8,
            2,
            3,
            4,
        ]
    )
)


# 2
print(Solution().trimMean([1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]))
