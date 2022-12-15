from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            s = numbers[i] + numbers[j]
            if s == target:
                return [i + 1, j + 1]
            elif s > target:
                j -= 1
            else:
                i += 1
        return [-1, -1]


# [3.42]
print(
    Solution().twoSum(
        numbers=[
            12,
            83,
            104,
            129,
            140,
            184,
            199,
            300,
            306,
            312,
            321,
            325,
            341,
            344,
            349,
            356,
            370,
            405,
            423,
            444,
            446,
            465,
            471,
            491,
            500,
            506,
            508,
            530,
            539,
            543,
            569,
            591,
            606,
            607,
            612,
            614,
            623,
            627,
            645,
            662,
            670,
            685,
            689,
            726,
            731,
            737,
            744,
            747,
            764,
            773,
            778,
            787,
            802,
            805,
            811,
            819,
            829,
            841,
            879,
            905,
            918,
            918,
            929,
            955,
            997,
        ],
        target=789,
    )
)

# [3.6]
print(Solution().twoSum(numbers=[3, 24, 50, 79, 88, 150, 345], target=200))

# [1.2]
print(Solution().twoSum(numbers=[0, 0, 3, 4], target=0))

# [1.2]
print(Solution().twoSum(numbers=[2, 7, 11, 15], target=9))

# [1.3]
print(Solution().twoSum(numbers=[2, 3, 4], target=6))

# [1.2]
print(Solution().twoSum(numbers=[-1, 0], target=-1))
