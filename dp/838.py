from math import floor


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # 在开头添加一个向左倾倒的哨兵
        dominoes = "L" + dominoes
        # 指示操作范围的左右指针
        left, right = 0, 1
        # 设置存放结果的数组
        ans = ["."] * len(dominoes)
        # 左侧指针超出元素数量后退出
        while left < len(dominoes):
            # 左侧指针指示的倾倒方向
            leftValue = dominoes[left]

            # 依次向右查找第一个非 . 字符的索引
            while right < len(dominoes) and dominoes[right] == ".":
                right += 1

            # 索引等于数量时设置空字符串表示已到边界
            if right == len(dominoes):
                rightValue = ""
            # 右侧指针指示的倾倒方向
            else:
                rightValue = dominoes[right]

            # 开始分情况判断范围内的倾倒
            # 左边向左倾倒，右边向左倾倒，所以范围内全部都是向左倾倒
            if leftValue == "L" and rightValue == "L":
                # 只需要处理左侧边界，右侧边界始终不要处理
                for i in range(left, right):
                    ans[i] = "L"
            # 左边向左倾倒，右边向右倾倒，所以范围内部全部保持不变
            elif leftValue == "L" and rightValue == "R":
                # 左侧边界需要设置倾倒
                ans[left] = "L"
            # 左边向右倾倒，右边向左倾倒，所以范围内左半部分向右倾倒，右边部分向左倾倒
            elif leftValue == "R" and rightValue == "L":
                # 半数元素的数量
                diff = (right - left + 1) / 2
                # 如果范围内元素的数量是偶数，就会出现小数
                diffInteger = floor(diff)
                # 判断当前元素的数量是否为偶数
                isEven = diff == diffInteger
                # 中间元素的索引值
                mid = left + diffInteger
                # 设置左半部分元素的倾倒方向为 R
                for i in range(left, mid):
                    ans[i] = "R"
                # 这里需要分情况处理
                # - 如果范围内元素的数目是奇数，那么右半部分的开始索引是 mid + 1，即需要跳过中间直立的元素
                # - 如果范围内元素的数目是偶数，那么右半部分的开始索引是 mid，即没有直立的元素
                for i in range(mid if isEven else (mid + 1), right):
                    ans[i] = "L"
            # 左边向右倾倒，右边向右倾倒，所以范围内全部都是向右倾倒
            elif leftValue == "R" and rightValue == "R":
                # 只需要处理左侧边界，右侧边界始终不要处理
                for i in range(left, right):
                    ans[i] = "R"
            # 左边向左倾倒，右边达到边界，所以范围内全部保持不变
            elif leftValue == "L" and rightValue == "":
                # 左侧边界需要设置倾倒
                ans[left] = "L"
            # 左边向右倾倒，所以范围内全部都是向右倾倒
            else:
                for i in range(left, right):
                    ans[i] = "R"
            # 设置 right 指针指向的元素为新的 left 边界
            left = right
            # 设置 right 指针下一个值为新的 right 边界
            right += 1
        return "".join(ans[i] for i in range(1, len(ans)))


# "LL.RR.LLRRLL.."
print(Solution().pushDominoes(".L.R...LR..L.."))

# "RR.L"
print(Solution().pushDominoes("RR.L"))
