from typing import List, Dict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic: Dict[int, int] = {}
        for index, value in enumerate(nums):
            if value in dic:
                return [dic[value], index]
            else:
                dic[target - value] = index
        return []


print(Solution().twoSum([2, 7, 11, 15], 9))
