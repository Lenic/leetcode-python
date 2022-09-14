from typing import List


class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        data = s[1:-1]
        res: List[str] = []

        def getValue(data: str):
            """获得数字的各种情况"""
            res: List[str] = []
            # 只有一位时只有一种情况
            if len(data) == 1:
                res.append(data)
            # 第一个字符为 0 时需要特殊处理
            elif data[0] == "0":
                # 第一个字符为 0 最后一个字符不是 0 说明必须是小数才成立，并且小数点在第一位的后面
                if data[-1] != "0":
                    res.append(f"{data[0]}.{data[1:]}")
                # 首尾都是 0 说明数字异常不可用，不加入结果
            else:
                # 从左侧分到一个数字开始，到右侧分到一个数字结束
                for i in range(1, len(data)):
                    left = data[:i]
                    right = data[i:]
                    # 右侧最后一个数字是 0 表示必须是整数才能成立，也就是不带小数点的情况
                    if right[-1] != "0":
                        res.append(f"{left}.{right}")
                # 还有一种情况就是全部分到左侧或者右侧，也就是不带小数点的情况
                res.append(data)
            return res

        for i in range(1, len(data)):
            leftList = getValue(data[:i])
            rightList = getValue(data[i:])

            for l in leftList:
                for r in rightList:
                    res.append(f"({l}, {r})")

        return res


# ["(0, 1.01)","(0, 10.1)","(0, 101)","(0.1, 0.1)"]
print(Solution().ambiguousCoordinates("(0101)"))

# ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]
print(Solution().ambiguousCoordinates("(123)"))
