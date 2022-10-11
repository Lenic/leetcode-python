from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            # 相等直接返回结果
            if nums[mid] == target:
                return mid
            # 左侧是单调递增
            if nums[left] <= nums[mid]:
                # 目标位置处于这个区间
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                # 获取 `mid` 右侧索引的值
                midRight = min(mid + 1, right)
                # 目标位置处于这个区间
                if nums[midRight] <= target <= nums[right]:
                    left = midRight
                else:
                    right = mid
        return -1


# 1
print(Solution().search([1, 3], 3))

# 113
print(
    Solution().search(
        [
            57,
            58,
            59,
            62,
            63,
            66,
            68,
            72,
            73,
            74,
            75,
            76,
            77,
            78,
            80,
            81,
            86,
            95,
            96,
            97,
            98,
            100,
            101,
            102,
            103,
            110,
            119,
            120,
            121,
            123,
            125,
            126,
            127,
            132,
            136,
            144,
            145,
            148,
            149,
            151,
            152,
            160,
            161,
            163,
            166,
            168,
            169,
            170,
            173,
            174,
            175,
            178,
            182,
            188,
            189,
            192,
            193,
            196,
            198,
            199,
            200,
            201,
            202,
            212,
            218,
            219,
            220,
            224,
            225,
            229,
            231,
            232,
            234,
            237,
            238,
            242,
            248,
            249,
            250,
            252,
            253,
            254,
            255,
            257,
            260,
            266,
            268,
            270,
            273,
            276,
            280,
            281,
            283,
            288,
            290,
            291,
            292,
            294,
            295,
            298,
            299,
            4,
            10,
            13,
            15,
            16,
            17,
            18,
            20,
            22,
            25,
            26,
            27,
            30,
            31,
            34,
            38,
            39,
            40,
            47,
            53,
            54,
        ],
        30,
    )
)

# 2
print(Solution().search([4, 5, 1, 2, 3], 1))

# 0
print(Solution().search([1, 3, 5], 1))

# 0
print(Solution().search([1], 1))

# -1
print(Solution().search([1], 0))

# -1
print(Solution().search([4, 5, 6, 7, 0, 1, 2], 3))

# 4
print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))
