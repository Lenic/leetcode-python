from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans, carry = [], 1
        for i in range(len(digits) - 1, -1, -1):
            s = digits[i] + carry
            carry = s // 10
            s = s if s < 10 else s - 10
            ans.append(s)
        if carry > 0:
            ans.append(carry)
        ans.reverse()
        return ans


# [4,3,2,2]
print(Solution().plusOne([4, 3, 2, 1]))

# [1,0,0]
print(Solution().plusOne([9, 9]))

# [1,2,4]
print(Solution().plusOne([1, 2, 3]))
