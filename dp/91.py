class Solution:
    # 数字 0 的 ASCII 码：计算数字时以此为基础
    minValue = ord("0")

    def numDecodings(self, s: str) -> int:
        # 第一个数字为 0 时直接退出
        if s[0] == "0":
            return 0

        # 滚动数组设置：初始化时 left 设置为 0，right 设置为 1 表示第一个数字时只有一种情况
        left, right = 0, 1
        # 第一个空格为哨兵：转换为数字后肯定不会符合要求，避免了循环时 if 判断
        converted = " " + s
        # 从真实的第一个数字开始循环
        for i in range(1, len(converted)):
            # 定义结果的默认值
            ans = 0
            # 将当前索引的字符串转换为数字判断
            current = ord(converted[i]) - self.minValue
            # 如果数字在 [1, 9] 范围表示可以接续前面的情况，即可表示的总数量没有发生改变
            if 1 <= current <= 9:
                ans = right
            # 计算索引 i 和 i - 1 两位数字的值：如果处于 [10, 26] 区间表示还有一种情况，此时和索引 i - 2 的数量相同，结果叠加
            double = (ord(converted[i - 1]) - self.minValue) * 10 + current
            if 10 <= double <= 26:
                ans += left
            # 重新设置滚动数组
            left, right = right, ans
        # 返回滚动数组的最后一个值，即最终的总数量
        return right


# 5
print(Solution().numDecodings("1123"))

# 1
print(Solution().numDecodings("27"))

# 1
print(Solution().numDecodings("10"))

# 1
print(Solution().numDecodings("110"))

# 1
print(Solution().numDecodings("810"))

# 2
print(Solution().numDecodings("11106"))

# 2
print(Solution().numDecodings("12"))

# 3
print(Solution().numDecodings("226"))

# 0
print(Solution().numDecodings("0"))
