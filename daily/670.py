from typing import List


class Solution:
    def maximumSwap(self, num: int) -> int:
        data: List[int] = [int(val) for val in list(str(num))]

        def getMaxIndex(index: int):
            """在 index 参数指定的索引开始（包含）查找最大数字的索引"""
            max: int = -1
            maxIndex: int = -1
            for i in range(index, len(data)):
                # 保证在所有最大值中取最后一个
                if max <= data[i]:
                    max = data[i]
                    maxIndex = i
            return maxIndex

        def dfs(index: int) -> bool:
            """递归修改原始数组：False 表示交换过元素"""
            if index == len(data):
                return True

            maxIndex = getMaxIndex(index)
            # 1. 第一个数字就是最大值时，还需要判断后续元素
            # 2. 第一个数字和 maxIndex 相等时，还需要判断后续元素
            #    - 这里不能直接和第二个数字交换的原因是可能连续存在多个相同的元素
            if maxIndex == index:
                return dfs(index + 1)
            elif data[maxIndex] == data[index]:
                while True:
                    index += 1
                    if data[maxIndex] != data[index]:
                        break
                    if index == maxIndex:
                        break
                if index == maxIndex:
                    return dfs(index + 1)

            data[index], data[maxIndex] = data[maxIndex], data[index]
            return False

        if dfs(0):
            return num

        res: int = 0
        for i in data:
            res = res * 10 + i
        return res


# 11
print(Solution().maximumSwap(11))

# 9973
print(Solution().maximumSwap(9973))

# 98863
print(Solution().maximumSwap(98368))

# 9913
print(Solution().maximumSwap(1993))

# 52341342
print(Solution().maximumSwap(22341345))

# 151
print(Solution().maximumSwap(115))

# 7236
print(Solution().maximumSwap(2736))
