from math import ceil
from typing import Dict, List


class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        res: List[int] = []
        cache: Dict[str, bool] = {}
        maxValue = 2**31

        def dfs(ans: List[int], index: int, unconfirmed: int) -> bool:
            # 缓存
            cacheKey = f'{"-".join(str(val) for val in ans)}:{index}:{unconfirmed}'
            if cacheKey in cache:
                return cache[cacheKey]

            def inner():
                if index == len(num):
                    # 所有元素都确认了，才表示已经找到了正确路径
                    # 数组的数量至少 3 个才达到要求
                    if unconfirmed == 0 and len(ans) > 2:
                        nonlocal res
                        res = ans[:]
                        return True
                    # 否则就表示失败，返回上一步处理
                    return False

                # 用于在循环中保存上一次的未确认结果
                currentUnconfirmed: int = unconfirmed
                # 计算循环的最大索引
                # - 第一个数字不能超过半数的字符，超过了就肯定不符合要求，因为后面的数字应该比前面的更大
                # - 第二个数字不能超过 2/3 的字符，超过了就肯定不符合要求，因为后面的数字应该比前面的更大
                max = len(num)
                if len(ans) == 0:
                    max = ceil(max / 2)
                elif len(ans) == 1:
                    max = max - max // 3
                for i in range(index, max):
                    # 当前索引的数字
                    val = ord(num[i]) - ord("0")
                    # 获取最后一个确认元素的值
                    # - 必须是存在两个时的最后一个
                    # - 只有一个或者没有时返回初始值 -1
                    # 初始值为 -1 用于和其它正常值区分
                    last = -1 if len(ans) < 2 else ans[-1]
                    # 填充前两个有些特殊
                    if len(ans) < 2:
                        # 首先判断当前索引的数字是否为 0，等于 0 需要特殊处理
                        # 进一步判断 last 是否为初始值 -1
                        # 还有个条件是前置未确认的值为 0，三个条件都满足才需要特殊处理
                        if val == 0 and last < 0 and currentUnconfirmed == 0:
                            next = currentUnconfirmed * 10
                            if next > maxValue:
                                return False
                            ans.append(next)
                            # 此时必须确认，因为数字前不允许有 0 前导
                            # 所以无论成功失败，都交给进一步的判断了
                            try:
                                return dfs(ans, i + 1, 0)
                            finally:
                                ans.pop()
                        # 如果不需要特殊处理则走正常逻辑
                        next = currentUnconfirmed * 10 + val
                        if next > maxValue:
                            return False
                        # 先尝试确认
                        ans.append(next)
                        # 如果能够找到直接返回，不再尝试其它可能
                        if dfs(ans, i + 1, 0):
                            return True
                        # 如果没有找到，首先回退上面尝试确认的内容
                        currentUnconfirmed = ans.pop()
                        # 如果能够找到直接返回，不再尝试其它可能
                        if dfs(ans, i + 1, currentUnconfirmed):
                            return True
                        # 如果没有找到，索引 +1 继续判断
                    # 正常判断条件
                    else:
                        # 获取 last 的前一个确认的值，这个时候 ans 中的数据至少有两个
                        previous = ans[-2]
                        # 获取倒数第二个和最后一个元素之和，即目标值
                        target = previous + last
                        # 首先判断当前索引的数字是否为 0，等于 0 需要特殊处理
                        # 进一步判断 currentUnconfirmed 是否等于 0，和上一个条件一起满足才需要特殊处理
                        if val == 0 and currentUnconfirmed == 0:
                            # 首先判断目标值是否也等于 0，不等于表示失败，回退到上一步处理
                            if target != 0:
                                return False
                            # 这里必须要确认
                            ans.append(0)
                            # 成功失败都靠接下来的判断了
                            try:
                                return dfs(ans, i + 1, 0)
                            finally:
                                ans.pop()
                        # 然后开始正常的判断
                        # 更新 currentUnconfirmed 加上当前值
                        currentUnconfirmed = currentUnconfirmed * 10 + val
                        if currentUnconfirmed > maxValue:
                            return False
                        # 如果加上当前值之后仍然小于目标值，则交给进一步的判断
                        if currentUnconfirmed < target:
                            if dfs(ans, i + 1, currentUnconfirmed):
                                return True
                            # 如果进一步判断失败，则继续循环
                        # 如果加上当前值之后大于目标值，则说明当前判断错误，回退上一步处理
                        elif currentUnconfirmed > target:
                            return False
                        # 等于说明应该确认了
                        else:
                            # 确认当前未确认的值
                            ans.append(currentUnconfirmed)
                            # 然后开启下一个数字的判断，无论成功失败这个判断结束，回退到上一步处理
                            try:
                                return dfs(ans, i + 1, 0)
                            finally:
                                ans.pop()

                # 循环结束后仍然没有确认表示找不到了
                return False

            value = inner()
            cache[cacheKey] = value
            return value

        dfs([], 0, 0)
        return res


# []
print(
    Solution().splitIntoFibonacci(
        "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"
    )
)

# [123,456,579][123,456,579]
print(Solution().splitIntoFibonacci("123456579"))

# [13205, 8, 13213, 13221, 26434, 39655, 66089, 105744, 171833, 277577]
print(Solution().splitIntoFibonacci("1320581321313221264343965566089105744171833277577"))

# [11,0,11,11]
print(Solution().splitIntoFibonacci("1101111"))

# []
print(Solution().splitIntoFibonacci("112358130"))

# []
print(Solution().splitIntoFibonacci("0123"))
